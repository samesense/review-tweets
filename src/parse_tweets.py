import json

import click
from urlextract import URLExtract

extractor = URLExtract()


def parse_like_js(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        # Remove the JavaScript assignment part
        data = f.read().replace("window.YTD.like.part0 = ", "")
        likes = json.loads(data)
        return likes


def try_https(text):
    # Find the first URL in the text
    start = text.find("https://")
    if start == -1:
        return None
    end = text.find(" ", start)
    if end == -1:
        end = len(text)
    return text[start:end]


def get_url(text):
    urls = extractor.find_urls(text)
    return urls
    # if 'http'
    # if "https://" in text:
    #     return try_https(text)
    #
    # # Find the first URL in the text
    # start = text.find("http://")
    # if start == -1:
    #     return None
    # end = text.find(" ", start)
    # if end == -1:
    #     end = len(text)
    # return text[start:end]


@click.command()
@click.argument("js", type=click.Path(exists=True))
@click.argument("out", type=str)
def main(js, out):
    likes_data = parse_like_js(js)
    with open(out, "w") as fout:
        print("tweetId\turl", file=fout)
        for like in likes_data:
            like = like["like"]
            if "fullText" in like:
                urls = get_url(like["fullText"])
                if urls:  # "http" in like["fullText"]:
                    if "1709213296052625530" == like["tweetId"]:
                        print(like)
                    t = like["tweetId"]
                    url = ";".join(urls)
                    print(f"{t}\t{url}", file=fout)


if __name__ == "__main__":
    main()
