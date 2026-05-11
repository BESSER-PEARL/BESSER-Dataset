





import java.util.List;
import java.util.ArrayList;

public class db_DocumentRoot  {

    private String mixed;
    private String specialFeatures;
    private String language;





    private List<db_CustomerReviewType> db_customerreviewtypes;




    private List<db_CustomerType> db_customertypes;




    private List<db_MovieDBType> db_moviedbtypes;




    private List<db_CriticsReviewType> db_criticsreviewtypes;


    public db_DocumentRoot(
        String mixed,        String specialFeatures,        String language    ) {
        this.mixed = mixed;
        this.specialFeatures = specialFeatures;
        this.language = language;
        this.db_customerreviewtypes = new ArrayList<>();
        this.db_customertypes = new ArrayList<>();
        this.db_moviedbtypes = new ArrayList<>();
        this.db_criticsreviewtypes = new ArrayList<>();
    }

    public db_DocumentRoot(
        String mixed,        String specialFeatures,        String language        ArrayList<db_CustomerReviewType> db_customerreviewtypes,        ArrayList<db_CustomerType> db_customertypes,        ArrayList<db_MovieDBType> db_moviedbtypes,        ArrayList<db_CriticsReviewType> db_criticsreviewtypes    ) {
        this.mixed = mixed;
        this.specialFeatures = specialFeatures;
        this.language = language;
        this.db_customerreviewtypes = db_customerreviewtypes;
        this.db_customertypes = db_customertypes;
        this.db_moviedbtypes = db_moviedbtypes;
        this.db_criticsreviewtypes = db_criticsreviewtypes;
    }

    public String getMixed() {
        return mixed;
    }

    public void setMixed(String mixed) {
        this.mixed = mixed;
    }
    public String getSpecialfeatures() {
        return specialFeatures;
    }

    public void setSpecialfeatures(String specialFeatures) {
        this.specialFeatures = specialFeatures;
    }
    public String getLanguage() {
        return language;
    }

    public void setLanguage(String language) {
        this.language = language;
    }

    public List<db_CustomerReviewType> getDb_customerreviewtypes() {
        return db_customerreviewtypes;
    }

    public void addDb_customerreviewtype(Db_customerreviewtype db_customerreviewtype) {
        this.db_customerreviewtypes.add(db_customerreviewtype);
    }
    public List<db_CustomerType> getDb_customertypes() {
        return db_customertypes;
    }

    public void addDb_customertype(Db_customertype db_customertype) {
        this.db_customertypes.add(db_customertype);
    }
    public List<db_MovieDBType> getDb_moviedbtypes() {
        return db_moviedbtypes;
    }

    public void addDb_moviedbtype(Db_moviedbtype db_moviedbtype) {
        this.db_moviedbtypes.add(db_moviedbtype);
    }
    public List<db_CriticsReviewType> getDb_criticsreviewtypes() {
        return db_criticsreviewtypes;
    }

    public void addDb_criticsreviewtype(Db_criticsreviewtype db_criticsreviewtype) {
        this.db_criticsreviewtypes.add(db_criticsreviewtype);
    }

}