





import java.util.List;
import java.util.ArrayList;

public class UML_14_AssociationEnd extends NamedElement {

    private String isNavigable;
    private String visibility;





    private UML_14_Association uml_14_association;




    private UML_14_Association uml_14_association;


    public UML_14_AssociationEnd(
        String isNavigable,        String visibility    ) {
        super(
        );
        this.isNavigable = isNavigable;
        this.visibility = visibility;
    }


    public String getIsnavigable() {
        return isNavigable;
    }

    public void setIsnavigable(String isNavigable) {
        this.isNavigable = isNavigable;
    }
    public String getVisibility() {
        return visibility;
    }

    public void setVisibility(String visibility) {
        this.visibility = visibility;
    }

    public UML_14_Association getUml_14_association() {
        return uml_14_association;
    }

    public void setUml_14_association(UML_14_Association uml_14_association) {
        this.uml_14_association = uml_14_association;
    }
    public UML_14_Association getUml_14_association() {
        return uml_14_association;
    }

    public void setUml_14_association(UML_14_Association uml_14_association) {
        this.uml_14_association = uml_14_association;
    }

}