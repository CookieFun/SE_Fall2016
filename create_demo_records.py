# -*- coding: utf-8 -*-
from HITIntEvents.wsgi import *
from event.models import Column, Event


def main():
    columns_urls = [('公告', 'notice'), ('记录', 'report')]

    for column_name, url in columns_urls:
        c = Column.objects.get_or_create(name=column_name, slug=url)[0]
        print("!")
        for i in range(1, 11):
            event = Event.objects.get_or_create(
                title='{}_{}'.format(column_name, i),
                slug='event_{}'.format(i),
                content='内容:{} {}'.format(column_name, i)
            )[0]
            event.column.add(c)
            # for k in event.column.all():
            #     print(k.name)


if __name__ == '__main__':
    main()
    print("Done!")
