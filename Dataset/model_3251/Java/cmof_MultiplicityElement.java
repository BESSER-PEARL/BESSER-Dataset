





import java.util.List;
import java.util.ArrayList;

public class cmof_MultiplicityElement extends Element {

    private String isOrdered;
    private String lower;
    private String isUnique;
    private String upper;





    private cmof_ValueSpecification cmof_valuespecification;




    private cmof_ValueSpecification cmof_valuespecification;


    public cmof_MultiplicityElement(
        String isOrdered,        String lower,        String isUnique,        String upper    ) {
        super(
        );
        this.isOrdered = isOrdered;
        this.lower = lower;
        this.isUnique = isUnique;
        this.upper = upper;
    }


    public String getIsordered() {
        return isOrdered;
    }

    public void setIsordered(String isOrdered) {
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

    public cmof_ValueSpecification getCmof_valuespecification() {
        return cmof_valuespecification;
    }

    public void setCmof_valuespecification(cmof_ValueSpecification cmof_valuespecification) {
        this.cmof_valuespecification = cmof_valuespecification;
    }
    public cmof_ValueSpecification getCmof_valuespecification() {
        return cmof_valuespecification;
    }

    public void setCmof_valuespecification(cmof_ValueSpecification cmof_valuespecification) {
        this.cmof_valuespecification = cmof_valuespecification;
    }

}