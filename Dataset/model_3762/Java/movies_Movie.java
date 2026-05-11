





import java.util.List;
import java.util.ArrayList;

public class movies_Movie  {

    private String genre;
    private String summary;
    private String title;
    private String actors;
    private String director;





    private List<movies_CriticsReview> movies_criticsreviews;




    private List<movies_Copy> movies_copys;


    public movies_Movie(
        String genre,        String summary,        String title,        String actors,        String director    ) {
        this.genre = genre;
        this.summary = summary;
        this.title = title;
        this.actors = actors;
        this.director = director;
        this.movies_criticsreviews = new ArrayList<>();
        this.movies_copys = new ArrayList<>();
    }

    public movies_Movie(
        String genre,        String summary,        String title,        String actors,        String director        ArrayList<movies_CriticsReview> movies_criticsreviews,        ArrayList<movies_Copy> movies_copys    ) {
        this.genre = genre;
        this.summary = summary;
        this.title = title;
        this.actors = actors;
        this.director = director;
        this.movies_criticsreviews = movies_criticsreviews;
        this.movies_copys = movies_copys;
    }

    public String getGenre() {
        return genre;
    }

    public void setGenre(String genre) {
        this.genre = genre;
    }
    public String getSummary() {
        return summary;
    }

    public void setSummary(String summary) {
        this.summary = summary;
    }
    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }
    public String getActors() {
        return actors;
    }

    public void setActors(String actors) {
        this.actors = actors;
    }
    public String getDirector() {
        return director;
    }

    public void setDirector(String director) {
        this.director = director;
    }

    public List<movies_CriticsReview> getMovies_criticsreviews() {
        return movies_criticsreviews;
    }

    public void addMovies_criticsreview(Movies_criticsreview movies_criticsreview) {
        this.movies_criticsreviews.add(movies_criticsreview);
    }
    public List<movies_Copy> getMovies_copys() {
        return movies_copys;
    }

    public void addMovies_copy(Movies_copy movies_copy) {
        this.movies_copys.add(movies_copy);
    }

}