





import java.util.List;
import java.util.ArrayList;

public class UML_14_AssociationEnd extends NamedElement {

    private String isNavigable;
    private String visibility;





    private UML_14_MultiplicityRange uml_14_multiplicityrange;




    private UML_14_Class uml_14_class;




    private UML_14_Attribute uml_14_attribute;


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

    public UML_14_MultiplicityRange getUml_14_multiplicityrange() {
        return uml_14_multiplicityrange;
    }

    public void setUml_14_multiplicityrange(UML_14_MultiplicityRange uml_14_multiplicityrange) {
        this.uml_14_multiplicityrange = uml_14_multiplicityrange;
    }
    public UML_14_Class getUml_14_class() {
        return uml_14_class;
    }

    public void setUml_14_class(UML_14_Class uml_14_class) {
        this.uml_14_class = uml_14_class;
    }
    public UML_14_Attribute getUml_14_attribute() {
        return uml_14_attribute;
    }

    public void setUml_14_attribute(UML_14_Attribute uml_14_attribute) {
        this.uml_14_attribute = uml_14_attribute;
    }

}