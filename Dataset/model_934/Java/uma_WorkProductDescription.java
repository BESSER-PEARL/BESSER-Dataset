





import java.util.List;
import java.util.ArrayList;

public class uma_WorkProductDescription extends ContentDescription {

    private String reasonsForNotNeeding;
    private String impactOfNotHaving;
    private String purpose;



    public uma_WorkProductDescription(
        String reasonsForNotNeeding,        String impactOfNotHaving,        String purpose    ) {
        super(
        );
        this.reasonsForNotNeeding = reasonsForNotNeeding;
        this.impactOfNotHaving = impactOfNotHaving;
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
    public String getPurpose() {
        return purpose;
    }

    public void setPurpose(String purpose) {
        this.purpose = purpose;
    }


}