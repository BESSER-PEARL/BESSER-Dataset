





import java.util.List;
import java.util.ArrayList;

public class smif_metadata_Definition extends Metadata {

    private String summaryDescription;
    private String textDefinition;





    private IdentifiableEntity identifiableentity;


    public smif_metadata_Definition(
        String summaryDescription,        String textDefinition    ) {
        super(
        );
        this.summaryDescription = summaryDescription;
        this.textDefinition = textDefinition;
    }


    public String getSummarydescription() {
        return summaryDescription;
    }

    public void setSummarydescription(String summaryDescription) {
        this.summaryDescription = summaryDescription;
    }
    public String getTextdefinition() {
        return textDefinition;
    }

    public void setTextdefinition(String textDefinition) {
        this.textDefinition = textDefinition;
    }

    public IdentifiableEntity getIdentifiableentity() {
        return identifiableentity;
    }

    public void setIdentifiableentity(IdentifiableEntity identifiableentity) {
        this.identifiableentity = identifiableentity;
    }

}