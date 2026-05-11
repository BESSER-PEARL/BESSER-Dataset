





import java.util.List;
import java.util.ArrayList;

public class simpleUML_MM_Attribute  {

    private String name;
    private boolean is_primary;





    private simpleUML_MM_Classifier simpleuml_mm_classifier;




    private simpleUML_MM_Class simpleuml_mm_class;


    public simpleUML_MM_Attribute(
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

    public simpleUML_MM_Classifier getSimpleuml_mm_classifier() {
        return simpleuml_mm_classifier;
    }

    public void setSimpleuml_mm_classifier(simpleUML_MM_Classifier simpleuml_mm_classifier) {
        this.simpleuml_mm_classifier = simpleuml_mm_classifier;
    }
    public simpleUML_MM_Class getSimpleuml_mm_class() {
        return simpleuml_mm_class;
    }

    public void setSimpleuml_mm_class(simpleUML_MM_Class simpleuml_mm_class) {
        this.simpleuml_mm_class = simpleuml_mm_class;
    }

}