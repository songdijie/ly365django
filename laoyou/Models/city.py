"""
# city.py.

# do the city
"""

from django.db import models


class City(models.Model):
    """
    City class implention.所在城市.

    property:
    """

    name = models.CharField(max_length=100)
    description = models.CharField(null=True, blank=True, max_length=250)
    cdate = models.DateTimeField(auto_now=True)
    member = models.PositiveIntegerField(default=0)

    def __str__(self):
        """__str__."""
        return "%s" % self.name


class CityCommunity(models.Model):
    """
    CityForum class implention.城市社区.

    property:
    """

    name = models.CharField(max_length=100)
    description = models.CharField(null=True, blank=True, max_length=250)
    cdate = models.DateTimeField(auto_now=True)

    city = models.ForeignKey(City, related_name='communitys', on_delete=models.CASCADE)

    def __str__(self):
        """__str__."""
        return "%d,%s" % (self.id, self.name)

class CityCommunityNews(models.Model):
    """
    CityNews.社区新闻.

    property
    """

    name = models.CharField(max_length=50)
    body = models.TextField()

    city_community = models.ForeignKey(CityCommunity, related_name='news', on_delete=models.CASCADE)

    def __str__(self):
        """__str__."""
        return "%s" % self.name


class CityCommunityNewsComment(models.Model):
    """
    CityCommunityNewsComment.

    property
    """

    news = models.ForeignKey(
        CityCommunityNews, related_name='comments', on_delete=models.CASCADE)
    comment = models.CharField(max_length=250)
    cdate = models.DateTimeField(auto_now=True)
    vote = models.PositiveIntegerField(default=0)

    def __str__(self):
        """__str__."""
        return "%s" % self.comment
