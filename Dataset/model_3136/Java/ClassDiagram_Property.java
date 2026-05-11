





import java.util.List;
import java.util.ArrayList;

public class ClassDiagram_Property  {

    private String name;
    private String aggregation;
    private String upper;
    private int lower;





    private ClassDiagram_Class classdiagram_class;




    private ClassDiagram_Classifier classdiagram_classifier;




    private ClassDiagram_Interface classdiagram_interface;




    private ClassDiagram_Association classdiagram_association;


    public ClassDiagram_Property(
        String name,        String aggregation,        String upper,        int lower    ) {
        this.name = name;
        this.aggregation = aggregation;
        this.upper = upper;
        this.lower = lower;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getAggregation() {
        return aggregation;
    }

    public void setAggregation(String aggregation) {
        this.aggregation = aggregation;
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

    public ClassDiagram_Class getClassdiagram_class() {
        return classdiagram_class;
    }

    public void setClassdiagram_class(ClassDiagram_Class classdiagram_class) {
        this.classdiagram_class = classdiagram_class;
    }
    public ClassDiagram_Classifier getClassdiagram_classifier() {
        return classdiagram_classifier;
    }

    public void setClassdiagram_classifier(ClassDiagram_Classifier classdiagram_classifier) {
        this.classdiagram_classifier = classdiagram_classifier;
    }
    public ClassDiagram_Interface getClassdiagram_interface() {
        return classdiagram_interface;
    }

    public void setClassdiagram_interface(ClassDiagram_Interface classdiagram_interface) {
        this.classdiagram_interface = classdiagram_interface;
    }
    public ClassDiagram_Association getClassdiagram_association() {
        return classdiagram_association;
    }

    public void setClassdiagram_association(ClassDiagram_Association classdiagram_association) {
        this.classdiagram_association = classdiagram_association;
    }

}