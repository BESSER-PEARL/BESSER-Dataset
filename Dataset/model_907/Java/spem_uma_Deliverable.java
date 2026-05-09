





import java.util.List;
import java.util.ArrayList;

public class spem_uma_Deliverable extends WorkProductUse {

    private String packagingGuidance;
    private String externalDescription;



    public spem_uma_Deliverable(
        String packagingGuidance,        String externalDescription    ) {
        super(
        );
        this.packagingGuidance = packagingGuidance;
        this.externalDescription = externalDescription;
    }


    public String getPackagingguidance() {
        return packagingGuidance;
    }

    public void setPackagingguidance(String packagingGuidance) {
        this.packagingGuidance = packagingGuidance;
    }
    public String getExternaldescription() {
        return externalDescription;
    }

    public void setExternaldescription(String externalDescription) {
        this.externalDescription = externalDescription;
    }


}