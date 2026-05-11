





import java.util.List;
import java.util.ArrayList;

public class movies_Place  {

    private String name;
    private String id;





    private movies_Copy movies_copy;




    private movies_MoviesDB movies_moviesdb;


    public movies_Place(
        String name,        String id    ) {
        this.name = name;
        this.id = id;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public movies_Copy getMovies_copy() {
        return movies_copy;
    }

    public void setMovies_copy(movies_Copy movies_copy) {
        this.movies_copy = movies_copy;
    }
    public movies_MoviesDB getMovies_moviesdb() {
        return movies_moviesdb;
    }

    public void setMovies_moviesdb(movies_MoviesDB movies_moviesdb) {
        this.movies_moviesdb = movies_moviesdb;
    }

}