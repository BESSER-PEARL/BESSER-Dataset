





import java.util.List;
import java.util.ArrayList;

public class libsys_Video extends Medium {

    private String genres;
    private String actors;



    public libsys_Video(
        String genres,        String actors    ) {
        super(
        );
        this.genres = genres;
        this.actors = actors;
    }


    public String getGenres() {
        return genres;
    }

    public void setGenres(String genres) {
        this.genres = genres;
    }
    public String getActors() {
        return actors;
    }

    public void setActors(String actors) {
        this.actors = actors;
    }


}