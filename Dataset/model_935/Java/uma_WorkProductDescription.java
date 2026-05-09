





import java.util.List;
import java.util.ArrayList;

public class uma_WorkProductDescription extends ContentDescription {

    private String purpose;
    private String impactOfNotHaving;
    private String reasonsForNotNeeding;



    public uma_WorkProductDescription(
        String purpose,        String impactOfNotHaving,        String reasonsForNotNeeding    ) {
        super(
        );
        this.purpose = purpose;
        this.impactOfNotHaving = impactOfNotHaving;
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
    public String getReasonsfornotneeding() {
        return reasonsForNotNeeding;
    }

    public void setReasonsfornotneeding(String reasonsForNotNeeding) {
        this.reasonsForNotNeeding = reasonsForNotNeeding;
    }


}