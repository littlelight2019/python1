# -*- coding: utf-8 -*-

import Movie_rating

def main():
    Movie_rating.readFiles()
    Movie_rating.getGenresList()
    Movie_rating.getRatingAndCountsByGenres()
    Movie_rating.getYearlyRatingStat()
    Movie_rating.makeMovieIdYearBin()
    Movie_rating.makeBoxplotYearBinRating()
    Movie_rating.getCountsAndRatingOverYears()
    
if __name__ == '__main__':
    main()