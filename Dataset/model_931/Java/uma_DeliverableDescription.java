





import java.util.List;
import java.util.ArrayList;

public class uma_DeliverableDescription extends WorkProductDescription {

    private String externalDescription;
    private String packagingGuidance;



    public uma_DeliverableDescription(
        String externalDescription,        String packagingGuidance    ) {
        super(
        );
        this.externalDescription = externalDescription;
        this.packagingGuidance = packagingGuidance;
    }


    public String getExternaldescription() {
        return externalDescription;
    }

    public void setExternaldescription(String externalDescription) {
        this.externalDescription = externalDescription;
    }
    public String getPackagingguidance() {
        return packagingGuidance;
    }

    public void setPackagingguidance(String packagingGuidance) {
        this.packagingGuidance = packagingGuidance;
    }


}