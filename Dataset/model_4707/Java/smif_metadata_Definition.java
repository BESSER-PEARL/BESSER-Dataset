





import java.util.List;
import java.util.ArrayList;

public class smif_metadata_Definition extends Metadata {

    private String textDefinition;
    private String summaryDescription;





    private IdentifiableEntity identifiableentity;


    public smif_metadata_Definition(
        String textDefinition,        String summaryDescription    ) {
        super(
        );
        this.textDefinition = textDefinition;
        this.summaryDescription = summaryDescription;
    }


    public String getTextdefinition() {
        return textDefinition;
    }

    public void setTextdefinition(String textDefinition) {
        this.textDefinition = textDefinition;
    }
    public String getSummarydescription() {
        return summaryDescription;
    }

    public void setSummarydescription(String summaryDescription) {
        this.summaryDescription = summaryDescription;
    }

    public IdentifiableEntity getIdentifiableentity() {
        return identifiableentity;
    }

    public void setIdentifiableentity(IdentifiableEntity identifiableentity) {
        this.identifiableentity = identifiableentity;
    }

}