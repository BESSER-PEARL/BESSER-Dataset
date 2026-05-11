





import java.util.List;
import java.util.ArrayList;

public class simpleUML_MM_Association  {

    private String name;





    private simpleUML_MM_ClassModel simpleuml_mm_classmodel;


    public simpleUML_MM_Association(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public simpleUML_MM_ClassModel getSimpleuml_mm_classmodel() {
        return simpleuml_mm_classmodel;
    }

    public void setSimpleuml_mm_classmodel(simpleUML_MM_ClassModel simpleuml_mm_classmodel) {
        this.simpleuml_mm_classmodel = simpleuml_mm_classmodel;
    }

}