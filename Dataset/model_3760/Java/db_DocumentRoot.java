





import java.util.List;
import java.util.ArrayList;

public class db_DocumentRoot  {

    private String specialFeatures;
    private String mixed;
    private String language;





    private List<db_CustomerReviewType> db_customerreviewtypes;


    public db_DocumentRoot(
        String specialFeatures,        String mixed,        String language    ) {
        this.specialFeatures = specialFeatures;
        this.mixed = mixed;
        this.language = language;
        this.db_customerreviewtypes = new ArrayList<>();
    }

    public db_DocumentRoot(
        String specialFeatures,        String mixed,        String language        ArrayList<db_CustomerReviewType> db_customerreviewtypes    ) {
        this.specialFeatures = specialFeatures;
        this.mixed = mixed;
        this.language = language;
        this.db_customerreviewtypes = db_customerreviewtypes;
    }

    public String getSpecialfeatures() {
        return specialFeatures;
    }

    public void setSpecialfeatures(String specialFeatures) {
        this.specialFeatures = specialFeatures;
    }
    public String getMixed() {
        return mixed;
    }

    public void setMixed(String mixed) {
        this.mixed = mixed;
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

}