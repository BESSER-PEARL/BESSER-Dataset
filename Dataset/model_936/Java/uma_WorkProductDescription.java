





import java.util.List;
import java.util.ArrayList;

public class uma_WorkProductDescription extends ContentDescription {

    private String purpose;
    private String reasonsForNotNeeding;
    private String impactOfNotHaving;



    public uma_WorkProductDescription(
        String purpose,        String reasonsForNotNeeding,        String impactOfNotHaving    ) {
        super(
        );
        this.purpose = purpose;
        this.reasonsForNotNeeding = reasonsForNotNeeding;
        this.impactOfNotHaving = impactOfNotHaving;
    }


    public String getPurpose() {
        return purpose;
    }

    public void setPurpose(String purpose) {
        this.purpose = purpose;
    }
    public String getReasonsfornotneeding() {
        return reasonsForNotNeeding;
    }

    public void setReasonsfornotneeding(String reasonsForNotNeeding) {
        this.reasonsForNotNeeding = reasonsForNotNeeding;
    }
    public String getImpactofnothaving() {
        return impactOfNotHaving;
    }

    public void setImpactofnothaving(String impactOfNotHaving) {
        this.impactOfNotHaving = impactOfNotHaving;
    }


}