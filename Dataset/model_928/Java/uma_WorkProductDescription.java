





import java.util.List;
import java.util.ArrayList;

public class uma_WorkProductDescription extends ContentDescription {

    private String reasonsForNotNeeding;
    private String purpose;
    private String impactOfNotHaving;



    public uma_WorkProductDescription(
        String reasonsForNotNeeding,        String purpose,        String impactOfNotHaving    ) {
        super(
        );
        this.reasonsForNotNeeding = reasonsForNotNeeding;
        this.purpose = purpose;
        this.impactOfNotHaving = impactOfNotHaving;
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


}