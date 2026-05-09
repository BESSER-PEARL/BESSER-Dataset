





import java.util.List;
import java.util.ArrayList;

public class UMLModel_MultiplicityElement extends Element {

    private String isUnique;
    private String lower;
    private String isOrdered;
    private String upper;





    private UMLModel_ValueSpecification umlmodel_valuespecification;




    private UMLModel_ValueSpecification umlmodel_valuespecification;


    public UMLModel_MultiplicityElement(
        String isUnique,        String lower,        String isOrdered,        String upper    ) {
        super(
        );
        this.isUnique = isUnique;
        this.lower = lower;
        this.isOrdered = isOrdered;
        this.upper = upper;
    }


    public String getIsunique() {
        return isUnique;
    }

    public void setIsunique(String isUnique) {
        this.isUnique = isUnique;
    }
    public String getLower() {
        return lower;
    }

    public void setLower(String lower) {
        this.lower = lower;
    }
    public String getIsordered() {
        return isOrdered;
    }

    public void setIsordered(String isOrdered) {
        this.isOrdered = isOrdered;
    }
    public String getUpper() {
        return upper;
    }

    public void setUpper(String upper) {
        this.upper = upper;
    }

    public UMLModel_ValueSpecification getUmlmodel_valuespecification() {
        return umlmodel_valuespecification;
    }

    public void setUmlmodel_valuespecification(UMLModel_ValueSpecification umlmodel_valuespecification) {
        this.umlmodel_valuespecification = umlmodel_valuespecification;
    }
    public UMLModel_ValueSpecification getUmlmodel_valuespecification() {
        return umlmodel_valuespecification;
    }

    public void setUmlmodel_valuespecification(UMLModel_ValueSpecification umlmodel_valuespecification) {
        this.umlmodel_valuespecification = umlmodel_valuespecification;
    }

}