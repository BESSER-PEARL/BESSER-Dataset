





import java.util.List;
import java.util.ArrayList;

public class uml2CD_Property extends NamedElement {

    private String isDerived;
    private String lower;
    private String upper;
    private String aggregation;





    private uml2CD_Association uml2cd_association;




    private uml2CD_Association uml2cd_association;


    public uml2CD_Property(
        String isDerived,        String lower,        String upper,        String aggregation    ) {
        super(
        );
        this.isDerived = isDerived;
        this.lower = lower;
        this.upper = upper;
        this.aggregation = aggregation;
    }


    public String getIsderived() {
        return isDerived;
    }

    public void setIsderived(String isDerived) {
        this.isDerived = isDerived;
    }
    public String getLower() {
        return lower;
    }

    public void setLower(String lower) {
        this.lower = lower;
    }
    public String getUpper() {
        return upper;
    }

    public void setUpper(String upper) {
        this.upper = upper;
    }
    public String getAggregation() {
        return aggregation;
    }

    public void setAggregation(String aggregation) {
        this.aggregation = aggregation;
    }

    public uml2CD_Association getUml2cd_association() {
        return uml2cd_association;
    }

    public void setUml2cd_association(uml2CD_Association uml2cd_association) {
        this.uml2cd_association = uml2cd_association;
    }
    public uml2CD_Association getUml2cd_association() {
        return uml2cd_association;
    }

    public void setUml2cd_association(uml2CD_Association uml2cd_association) {
        this.uml2cd_association = uml2cd_association;
    }

}