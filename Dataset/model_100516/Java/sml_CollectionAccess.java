





import java.util.List;
import java.util.ArrayList;

public class sml_CollectionAccess  {

    private String collectionOperation;





    private sml_FeatureAccess sml_featureaccess;


    public sml_CollectionAccess(
        String collectionOperation    ) {
        this.collectionOperation = collectionOperation;
    }


    public String getCollectionoperation() {
        return collectionOperation;
    }

    public void setCollectionoperation(String collectionOperation) {
        this.collectionOperation = collectionOperation;
    }

    public sml_FeatureAccess getSml_featureaccess() {
        return sml_featureaccess;
    }

    public void setSml_featureaccess(sml_FeatureAccess sml_featureaccess) {
        this.sml_featureaccess = sml_featureaccess;
    }

}