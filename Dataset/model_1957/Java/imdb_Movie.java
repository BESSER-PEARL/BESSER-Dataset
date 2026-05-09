




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class imdb_Movie  {

    private int runtime;
    private String genres;
    private int userRatings;
    private int age;
    private String synopsis;
    private String poster;
    private LocalDate releaseDate;
    private int metacriticReviews;
    private float rating;
    private String title;
    private int metaScore;
    private int criticReviews;
    private int userReviews;



    public imdb_Movie(
        int runtime,        String genres,        int userRatings,        int age,        String synopsis,        String poster,        LocalDate releaseDate,        int metacriticReviews,        float rating,        String title,        int metaScore,        int criticReviews,        int userReviews    ) {
        this.runtime = runtime;
        this.genres = genres;
        this.userRatings = userRatings;
        this.age = age;
        this.synopsis = synopsis;
        this.poster = poster;
        this.releaseDate = releaseDate;
        this.metacriticReviews = metacriticReviews;
        this.rating = rating;
        this.title = title;
        this.metaScore = metaScore;
        this.criticReviews = criticReviews;
        this.userReviews = userReviews;
    }


    public int getRuntime() {
        return runtime;
    }

    public void setRuntime(int runtime) {
        this.runtime = runtime;
    }
    public String getGenres() {
        return genres;
    }

    public void setGenres(String genres) {
        this.genres = genres;
    }
    public int getUserratings() {
        return userRatings;
    }

    public void setUserratings(int userRatings) {
        this.userRatings = userRatings;
    }
    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }
    public String getSynopsis() {
        return synopsis;
    }

    public void setSynopsis(String synopsis) {
        this.synopsis = synopsis;
    }
    public String getPoster() {
        return poster;
    }

    public void setPoster(String poster) {
        this.poster = poster;
    }
    public LocalDate getReleasedate() {
        return releaseDate;
    }

    public void setReleasedate(LocalDate releaseDate) {
        this.releaseDate = releaseDate;
    }
    public int getMetacriticreviews() {
        return metacriticReviews;
    }

    public void setMetacriticreviews(int metacriticReviews) {
        this.metacriticReviews = metacriticReviews;
    }
    public float getRating() {
        return rating;
    }

    public void setRating(float rating) {
        this.rating = rating;
    }
    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }
    public int getMetascore() {
        return metaScore;
    }

    public void setMetascore(int metaScore) {
        this.metaScore = metaScore;
    }
    public int getCriticreviews() {
        return criticReviews;
    }

    public void setCriticreviews(int criticReviews) {
        this.criticReviews = criticReviews;
    }
    public int getUserreviews() {
        return userReviews;
    }

    public void setUserreviews(int userReviews) {
        this.userReviews = userReviews;
    }


}