rule parse_tweets:
    input:
        RAW / 'data/like.js',
    output:
        INT / 'tweets.tsv',
    shell:
        'python parse_tweets.py {input} {output}'
