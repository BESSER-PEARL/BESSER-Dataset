





import java.util.List;
import java.util.ArrayList;

public class rapidml_ReferenceLink extends ReferenceTreatment {

    private String name;
    private String collectionRealizationLevel;





    private rapidml_LinkRelation rapidml_linkrelation;


    public rapidml_ReferenceLink(
        String name,        String collectionRealizationLevel    ) {
        super(
        );
        this.name = name;
        this.collectionRealizationLevel = collectionRealizationLevel;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getCollectionrealizationlevel() {
        return collectionRealizationLevel;
    }

    public void setCollectionrealizationlevel(String collectionRealizationLevel) {
        this.collectionRealizationLevel = collectionRealizationLevel;
    }

    public rapidml_LinkRelation getRapidml_linkrelation() {
        return rapidml_linkrelation;
    }

    public void setRapidml_linkrelation(rapidml_LinkRelation rapidml_linkrelation) {
        this.rapidml_linkrelation = rapidml_linkrelation;
    }

}