





import java.util.List;
import java.util.ArrayList;

public class db_MovieDBType  {

    private String movieDBFeatureMap;
    private String comment;



    public db_MovieDBType(
        String movieDBFeatureMap,        String comment    ) {
        this.movieDBFeatureMap = movieDBFeatureMap;
        this.comment = comment;
    }


    public String getMoviedbfeaturemap() {
        return movieDBFeatureMap;
    }

    public void setMoviedbfeaturemap(String movieDBFeatureMap) {
        this.movieDBFeatureMap = movieDBFeatureMap;
    }
    public String getComment() {
        return comment;
    }

    public void setComment(String comment) {
        this.comment = comment;
    }


}