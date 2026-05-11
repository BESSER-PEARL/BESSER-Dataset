





import java.util.List;
import java.util.ArrayList;

public class UmlMM_Property  {

    private String name;
    private int upper;
    private int lower;





    private UmlMM_Classifier umlmm_classifier;




    private UmlMM_Class umlmm_class;




    private UmlMM_Class umlmm_class;


    public UmlMM_Property(
        String name,        int upper,        int lower    ) {
        this.name = name;
        this.upper = upper;
        this.lower = lower;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getUpper() {
        return upper;
    }

    public void setUpper(int upper) {
        this.upper = upper;
    }
    public int getLower() {
        return lower;
    }

    public void setLower(int lower) {
        this.lower = lower;
    }

    public UmlMM_Classifier getUmlmm_classifier() {
        return umlmm_classifier;
    }

    public void setUmlmm_classifier(UmlMM_Classifier umlmm_classifier) {
        this.umlmm_classifier = umlmm_classifier;
    }
    public UmlMM_Class getUmlmm_class() {
        return umlmm_class;
    }

    public void setUmlmm_class(UmlMM_Class umlmm_class) {
        this.umlmm_class = umlmm_class;
    }
    public UmlMM_Class getUmlmm_class() {
        return umlmm_class;
    }

    public void setUmlmm_class(UmlMM_Class umlmm_class) {
        this.umlmm_class = umlmm_class;
    }

}