





import java.util.List;
import java.util.ArrayList;

public class uml2CD_Property extends NamedElement {

    private String upper;
    private String isDerived;
    private String aggregation;
    private String lower;



    public uml2CD_Property(
        String upper,        String isDerived,        String aggregation,        String lower    ) {
        super(
        );
        this.upper = upper;
        this.isDerived = isDerived;
        this.aggregation = aggregation;
        this.lower = lower;
    }


    public String getUpper() {
        return upper;
    }

    public void setUpper(String upper) {
        this.upper = upper;
    }
    public String getIsderived() {
        return isDerived;
    }

    public void setIsderived(String isDerived) {
        this.isDerived = isDerived;
    }
    public String getAggregation() {
        return aggregation;
    }

    public void setAggregation(String aggregation) {
        this.aggregation = aggregation;
    }
    public String getLower() {
        return lower;
    }

    public void setLower(String lower) {
        this.lower = lower;
    }


}