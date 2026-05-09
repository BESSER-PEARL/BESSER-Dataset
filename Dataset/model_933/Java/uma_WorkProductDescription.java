





import java.util.List;
import java.util.ArrayList;

public class uma_WorkProductDescription extends ContentDescription {

    private String impactOfNotHaving;
    private String reasonsForNotNeeding;
    private String purpose;



    public uma_WorkProductDescription(
        String impactOfNotHaving,        String reasonsForNotNeeding,        String purpose    ) {
        super(
        );
        this.impactOfNotHaving = impactOfNotHaving;
        this.reasonsForNotNeeding = reasonsForNotNeeding;
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
    public String getPurpose() {
        return purpose;
    }

    public void setPurpose(String purpose) {
        this.purpose = purpose;
    }


}