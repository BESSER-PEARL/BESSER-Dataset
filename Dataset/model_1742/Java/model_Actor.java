





import java.util.List;
import java.util.ArrayList;

public class model_Actor  {

    private String name;
    private int id;





    private model_Movie model_movie;




    private List<model_Movie> model_movies;


    public model_Actor(
        String name,        int id    ) {
        this.name = name;
        this.id = id;
        this.model_movies = new ArrayList<>();
    }

    public model_Actor(
        String name,        int id        ArrayList<model_Movie> model_movies    ) {
        this.name = name;
        this.id = id;
        this.model_movies = model_movies;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public model_Movie getModel_movie() {
        return model_movie;
    }

    public void setModel_movie(model_Movie model_movie) {
        this.model_movie = model_movie;
    }
    public List<model_Movie> getModel_movies() {
        return model_movies;
    }

    public void addModel_movie(Model_movie model_movie) {
        this.model_movies.add(model_movie);
    }

}