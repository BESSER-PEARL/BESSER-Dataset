





import java.util.List;
import java.util.ArrayList;

public class UML2_MultiplicityElement extends Element {

    private boolean isOrdered;
    private String upper;
    private int lower;
    private boolean isUnique;





    private UML2_ValueSpecification uml2_valuespecification;




    private UML2_ValueSpecification uml2_valuespecification;


    public UML2_MultiplicityElement(
        boolean isOrdered,        String upper,        int lower,        boolean isUnique    ) {
        super(
        );
        this.isOrdered = isOrdered;
        this.upper = upper;
        this.lower = lower;
        this.isUnique = isUnique;
    }


    public boolean getIsordered() {
        return isOrdered;
    }

    public void setIsordered(boolean isOrdered) {
        this.isOrdered = isOrdered;
    }
    public String getUpper() {
        return upper;
    }

    public void setUpper(String upper) {
        this.upper = upper;
    }
    public int getLower() {
        return lower;
    }

    public void setLower(int lower) {
        this.lower = lower;
    }
    public boolean getIsunique() {
        return isUnique;
    }

    public void setIsunique(boolean isUnique) {
        this.isUnique = isUnique;
    }

    public UML2_ValueSpecification getUml2_valuespecification() {
        return uml2_valuespecification;
    }

    public void setUml2_valuespecification(UML2_ValueSpecification uml2_valuespecification) {
        this.uml2_valuespecification = uml2_valuespecification;
    }
    public UML2_ValueSpecification getUml2_valuespecification() {
        return uml2_valuespecification;
    }

    public void setUml2_valuespecification(UML2_ValueSpecification uml2_valuespecification) {
        this.uml2_valuespecification = uml2_valuespecification;
    }

}