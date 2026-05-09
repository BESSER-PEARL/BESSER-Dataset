





import java.util.List;
import java.util.ArrayList;

public class RefUML_MultiplicityElement extends Element {

    private String lower;
    private String isUnique;
    private String upper;
    private String isOrdered;





    private RefUML_ValueSpecification refuml_valuespecification;




    private RefUML_ValueSpecification refuml_valuespecification;


    public RefUML_MultiplicityElement(
        String lower,        String isUnique,        String upper,        String isOrdered    ) {
        super(
        );
        this.lower = lower;
        this.isUnique = isUnique;
        this.upper = upper;
        this.isOrdered = isOrdered;
    }


    public String getLower() {
        return lower;
    }

    public void setLower(String lower) {
        this.lower = lower;
    }
    public String getIsunique() {
        return isUnique;
    }

    public void setIsunique(String isUnique) {
        this.isUnique = isUnique;
    }
    public String getUpper() {
        return upper;
    }

    public void setUpper(String upper) {
        this.upper = upper;
    }
    public String getIsordered() {
        return isOrdered;
    }

    public void setIsordered(String isOrdered) {
        this.isOrdered = isOrdered;
    }

    public RefUML_ValueSpecification getRefuml_valuespecification() {
        return refuml_valuespecification;
    }

    public void setRefuml_valuespecification(RefUML_ValueSpecification refuml_valuespecification) {
        this.refuml_valuespecification = refuml_valuespecification;
    }
    public RefUML_ValueSpecification getRefuml_valuespecification() {
        return refuml_valuespecification;
    }

    public void setRefuml_valuespecification(RefUML_ValueSpecification refuml_valuespecification) {
        this.refuml_valuespecification = refuml_valuespecification;
    }

}