





import java.util.List;
import java.util.ArrayList;

public class UMLModel_TimeEvent extends Event {

    private String isRelative;





    private UMLModel_ValueSpecification umlmodel_valuespecification;


    public UMLModel_TimeEvent(
        String isRelative    ) {
        super(
        );
        this.isRelative = isRelative;
    }


    public String getIsrelative() {
        return isRelative;
    }

    public void setIsrelative(String isRelative) {
        this.isRelative = isRelative;
    }

    public UMLModel_ValueSpecification getUmlmodel_valuespecification() {
        return umlmodel_valuespecification;
    }

    public void setUmlmodel_valuespecification(UMLModel_ValueSpecification umlmodel_valuespecification) {
        this.umlmodel_valuespecification = umlmodel_valuespecification;
    }

}