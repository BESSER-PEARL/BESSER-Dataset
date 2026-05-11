





import java.util.List;
import java.util.ArrayList;

public class db_MovieType  {

    private String any;
    private String director;
    private String genre;
    private String summary;
    private String title;
    private String iD;
    private String actors;
    private String criticsReviewGroup;





    private List<db_CriticsReviewType> db_criticsreviewtypes;




    private db_CustomerType db_customertype;




    private db_MovieDBType db_moviedbtype;


    public db_MovieType(
        String any,        String director,        String genre,        String summary,        String title,        String iD,        String actors,        String criticsReviewGroup    ) {
        this.any = any;
        this.director = director;
        this.genre = genre;
        this.summary = summary;
        this.title = title;
        this.iD = iD;
        this.actors = actors;
        this.criticsReviewGroup = criticsReviewGroup;
        this.db_criticsreviewtypes = new ArrayList<>();
    }

    public db_MovieType(
        String any,        String director,        String genre,        String summary,        String title,        String iD,        String actors,        String criticsReviewGroup        ArrayList<db_CriticsReviewType> db_criticsreviewtypes    ) {
        this.any = any;
        this.director = director;
        this.genre = genre;
        this.summary = summary;
        this.title = title;
        this.iD = iD;
        this.actors = actors;
        this.criticsReviewGroup = criticsReviewGroup;
        this.db_criticsreviewtypes = db_criticsreviewtypes;
    }

    public String getAny() {
        return any;
    }

    public void setAny(String any) {
        this.any = any;
    }
    public String getDirector() {
        return director;
    }

    public void setDirector(String director) {
        this.director = director;
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
    public String getId() {
        return iD;
    }

    public void setId(String iD) {
        this.iD = iD;
    }
    public String getActors() {
        return actors;
    }

    public void setActors(String actors) {
        this.actors = actors;
    }
    public String getCriticsreviewgroup() {
        return criticsReviewGroup;
    }

    public void setCriticsreviewgroup(String criticsReviewGroup) {
        this.criticsReviewGroup = criticsReviewGroup;
    }

    public List<db_CriticsReviewType> getDb_criticsreviewtypes() {
        return db_criticsreviewtypes;
    }

    public void addDb_criticsreviewtype(Db_criticsreviewtype db_criticsreviewtype) {
        this.db_criticsreviewtypes.add(db_criticsreviewtype);
    }
    public db_CustomerType getDb_customertype() {
        return db_customertype;
    }

    public void setDb_customertype(db_CustomerType db_customertype) {
        this.db_customertype = db_customertype;
    }
    public db_MovieDBType getDb_moviedbtype() {
        return db_moviedbtype;
    }

    public void setDb_moviedbtype(db_MovieDBType db_moviedbtype) {
        this.db_moviedbtype = db_moviedbtype;
    }

}