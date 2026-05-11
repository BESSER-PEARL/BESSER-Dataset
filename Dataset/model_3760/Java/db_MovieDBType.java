





import java.util.List;
import java.util.ArrayList;

public class db_MovieDBType  {

    private String comment;
    private String movieDBFeatureMap;





    private db_DocumentRoot db_documentroot;


    public db_MovieDBType(
        String comment,        String movieDBFeatureMap    ) {
        this.comment = comment;
        this.movieDBFeatureMap = movieDBFeatureMap;
    }


    public String getComment() {
        return comment;
    }

    public void setComment(String comment) {
        this.comment = comment;
    }
    public String getMoviedbfeaturemap() {
        return movieDBFeatureMap;
    }

    public void setMoviedbfeaturemap(String movieDBFeatureMap) {
        this.movieDBFeatureMap = movieDBFeatureMap;
    }

    public db_DocumentRoot getDb_documentroot() {
        return db_documentroot;
    }

    public void setDb_documentroot(db_DocumentRoot db_documentroot) {
        this.db_documentroot = db_documentroot;
    }

}