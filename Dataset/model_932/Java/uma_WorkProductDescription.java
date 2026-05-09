





import java.util.List;
import java.util.ArrayList;

public class uma_WorkProductDescription extends ContentDescription {

    private String reasonsForNotNeeding;
    private String purpose;
    private String impactOfNotHaving;
    private String externalId;



    public uma_WorkProductDescription(
        String reasonsForNotNeeding,        String purpose,        String impactOfNotHaving,        String externalId    ) {
        super(
        );
        this.reasonsForNotNeeding = reasonsForNotNeeding;
        this.purpose = purpose;
        this.impactOfNotHaving = impactOfNotHaving;
        this.externalId = externalId;
    }


    public String getReasonsfornotneeding() {
        return reasonsForNotNeeding;
    }

    public void setReasonsfornotneeding(String reasonsForNotNeeding) {
        this.reasonsForNotNeeding = reasonsForNotNeeding;
    }
    public String getPurpose() {
        return purpose;
    }

    public void setPurpose(String purpose) {
        this.purpose = purpose;
    }
    public String getImpactofnothaving() {
        return impactOfNotHaving;
    }

    public void setImpactofnothaving(String impactOfNotHaving) {
        this.impactOfNotHaving = impactOfNotHaving;
    }
    public String getExternalid() {
        return externalId;
    }

    public void setExternalid(String externalId) {
        this.externalId = externalId;
    }


}