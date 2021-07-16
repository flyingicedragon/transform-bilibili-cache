import os
import shutil
import json


class Cache:
    '''缓存根目录对象
    '''

    def __init__(self, cache_path: str, out_path: str) -> None:
        self.cache_path = cache_path
        self.out_path = out_path
        os.makedirs(self.out_path, exist_ok=True)
        self._get_projects()

    def _get_projects(self) -> None:
        self.projects_names = os.listdir(self.cache_path)
        for project in self.projects_names:
            Project(os.path.join(self.cache_path, project), self.out_path)


class Project:
    '''缓存项目对象
    '''
    def __init__(self, project_path: str, out_path: str) -> None:
        self.path = project_path
        self.out_path = out_path
        self._get_part()

    def _get_part(self) -> None:
        self.part_names = os.listdir(self.path)
        self._get_title()
        for part in self.part_names:
            Part(
                os.path.join(self.path, part),
                os.path.join(self.out_path, self.title)
            )

    def _get_title(self) -> None:
        information_path = os.path.join(
            self.path,
            self.part_names[0],
            'entry.json'
        )
        with open(information_path) as information_file:
            part0_information = json.load(information_file)
        self.title = part0_information['title']
        os.mkdir(os.path.join(self.out_path, self.title))


class Part:
    '''缓存项目的单个视频对象
    '''
    def __init__(self, part_path: str, out_path: str) -> None:
        self.path = part_path
        self.out_path = out_path
        self._get_name()
        self._get_video()

    def _get_name(self) -> None:
        information_path = os.path.join(self.path, 'entry.json')
        with open(information_path) as information_file:
            self.information = json.load(information_file)
        self.part = self.information['page_data']['part']

    def _get_video(self) -> None:
        self.video_path = os.path.join(
            self.path,
            self.information['type_tag'],
            '0.blv'
        )
        self.video_out = os.path.join(
            self.out_path,
            self.part + '.flv'
        )
        shutil.copyfile(self.video_path, self.video_out)
