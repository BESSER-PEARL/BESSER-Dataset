





import java.util.List;
import java.util.ArrayList;

public class UmlMM_Parameter  {

    private String name;





    private UmlMM_Operation umlmm_operation;




    private UmlMM_Classifier umlmm_classifier;




    private UmlMM_Operation umlmm_operation;


    public UmlMM_Parameter(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public UmlMM_Operation getUmlmm_operation() {
        return umlmm_operation;
    }

    public void setUmlmm_operation(UmlMM_Operation umlmm_operation) {
        this.umlmm_operation = umlmm_operation;
    }
    public UmlMM_Classifier getUmlmm_classifier() {
        return umlmm_classifier;
    }

    public void setUmlmm_classifier(UmlMM_Classifier umlmm_classifier) {
        this.umlmm_classifier = umlmm_classifier;
    }
    public UmlMM_Operation getUmlmm_operation() {
        return umlmm_operation;
    }

    public void setUmlmm_operation(UmlMM_Operation umlmm_operation) {
        this.umlmm_operation = umlmm_operation;
    }

}