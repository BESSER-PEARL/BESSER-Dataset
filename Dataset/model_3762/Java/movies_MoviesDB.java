





import java.util.List;
import java.util.ArrayList;

public class movies_MoviesDB  {

    private String comment;





    private List<movies_Movie> movies_movies;


    public movies_MoviesDB(
        String comment    ) {
        this.comment = comment;
        this.movies_movies = new ArrayList<>();
    }

    public movies_MoviesDB(
        String comment        ArrayList<movies_Movie> movies_movies    ) {
        this.comment = comment;
        this.movies_movies = movies_movies;
    }

    public String getComment() {
        return comment;
    }

    public void setComment(String comment) {
        this.comment = comment;
    }

    public List<movies_Movie> getMovies_movies() {
        return movies_movies;
    }

    public void addMovies_movie(Movies_movie movies_movie) {
        this.movies_movies.add(movies_movie);
    }

}