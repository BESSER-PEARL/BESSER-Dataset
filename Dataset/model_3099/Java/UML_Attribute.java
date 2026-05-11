





import java.util.List;
import java.util.ArrayList;

public class UML_Attribute  {

    private String name;
    private boolean is_primary;





    private UML_Classifier uml_classifier;




    private UML_Class uml_class;


    public UML_Attribute(
        String name,        boolean is_primary    ) {
        this.name = name;
        this.is_primary = is_primary;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getIs_primary() {
        return is_primary;
    }

    public void setIs_primary(boolean is_primary) {
        this.is_primary = is_primary;
    }

    public UML_Classifier getUml_classifier() {
        return uml_classifier;
    }

    public void setUml_classifier(UML_Classifier uml_classifier) {
        this.uml_classifier = uml_classifier;
    }
    public UML_Class getUml_class() {
        return uml_class;
    }

    public void setUml_class(UML_Class uml_class) {
        this.uml_class = uml_class;
    }

}