#!/usr/bin/env python

import json
import os

FILE_EXTENSION = '.json'

class FacebookProfile:

  def __init__(self, data_dir):
    self.__dict__ = self._profile = self._get_profile(data_dir)

  def __getitem__(self, key):
    return self._profile[key]

  def _get_profile(self, data_dir):
    """
    Creates a master dictionary of all other JSON objects in the data dir.
    @param data_dir: String
      Filepath of Facebook data directory root
    @return: Dictionary
      Dictionary of all downloaded data objects
    """
    profile_data = {}
    delim = os.path.sep
    for dir_path, _, files in os.walk(data_dir):
      relative_path = dir_path[len(data_dir)+len(delim):]
      for f in files:
        # If a JSON file
        if f.endswith(FILE_EXTENSION):
          dir_list = relative_path.split(delim)
          # Start building dictionary
          if dir_list[0] not in profile_data:
            profile_data[dir_list[0]] = {}
          cur_dict = profile_data[dir_list.pop(0)]
          # Build dictionary path based on file paths
          while len(dir_list) > 0:
            if dir_list[0] not in cur_dict:
              cur_dict[dir_list[0]] = {}
            cur_dict = cur_dict[dir_list.pop(0)]
          # Update dictionary with file contents
          if dir_path.endswith('photos'+delim+'album'):
            # Special case for enumerated albums
            filename = f[:-len(FILE_EXTENSION)]
            cur_dict[filename] = json.load(open(os.path.join(dir_path, f)))
          else:
            cur_dict.update(json.load(open(os.path.join(dir_path, f))))
    return profile_data
