import json
import xml.etree.ElementTree as et


class Song:
    def __init__(self, song_id, title, artist):
        self.song_id = song_id
        self.title = title
        self.artist = artist


class SongSerializer:
    def serialize(self, song, format):
        serializer = get_serializer(format)
        return serializer


def get_serializer(format):
    if format == 'JSON':
        return serialize_to_json(song)
    elif format == 'XML':
        return serialize_to_xml(song)
    else:
        raise ValueError(format)


def serialize_to_json(song):
    payload = {
        'id': song.song_id,
        'title': song.title,
        'artist': song.artist
    }
    return json.dumps(payload)


def serialize_to_xml(song):
    song_info = et.Element('song', attrib={'id': song.song_id})
    title = et.SubElement(song_info, 'title')
    title.text = song.title
    artist = et.SubElement(song_info, 'artist')
    artist.text = song.artist
    return et.tostring(song_info, encoding='unicode')


song = Song('1', 'Water of Love', 'Dire Straits')
serializer = SongSerializer()

pr_json = serializer.serialize(song, 'JSON')
print(pr_json)

xml = serializer.serialize(song, 'XML')
print(xml)

# IT a bed code
# import json
# import xml.etree.ElementTree as et
#
#
# class Song:
#     def __init__(self, song_id, title, artist):
#         self.song_id = song_id
#         self.title = title
#         self.artist = artist
#
#
# class SongSerializer:
#     def serialize(self, song, format):
#         if format == 'JSON':
#             song_info = {
#                 'id': song.song_id,
#                 'title': song.title,
#                 'artist': song.artist
#             }
#             return json.dumps(song_info)
#         elif format == 'XML':
#             song_info = et.Element('song', attrib={'id': song.song_id})
#             title = et.SubElement(song_info, 'title')
#             title.text = song.title
#             artist = et.SubElement(song_info, 'artist')
#             artist.text = song.artist
#             return et.tostring(song_info, encoding='unicode')
#         else:
#             raise ValueError(format)
#
#
# song = Song('1', 'Water of Love', 'Dire Straits')
# serializer = SongSerializer()
#
# json = serializer.serialize(song, 'JSON')
# print(json)
#
# xml = serializer.serialize(song, 'XML')
# print(xml)
#
# # yaml = serializer.serialize(song, 'YAML')
# # print(yaml)
