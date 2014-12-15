treehouse
=========

## Python scraper for downloading Treehouse videos. ##

**Dependencies**: *nix shell, python & curl

It requires a **valid** Treehouse account in order to have a token. **This token is unique for every user**

First go to the page of the course you want to extract videos from and copy the "iTunes Feed" link.

`python treehouse.py <paste the that link here>`

Ex:
`python treehouse.py itpc://teamtreehouse.com/library/wordpress-theme-development.rss?feed_token=<token>`

This will generate a list of curl commands to download the videos, and organize them into folders and appropiate names for the files. 

You can save the links into a file by using a redirection

`python treehouse.py itpc://teamtreehouse.com/library/wordpress-theme-development.rss?feed_token=itpc://teamtreehouse.com/library/wordpress-theme-development.rss?feed_token=aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee > wp-theme-dev.sh`


