





import java.util.List;
import java.util.ArrayList;

public class classDiagram_ElementType  {

    private boolean isCollection;





    private classDiagram_Attribute classdiagram_attribute;




    private classDiagram_Classifier classdiagram_classifier;




    private classDiagram_Method classdiagram_method;


    public classDiagram_ElementType(
        boolean isCollection    ) {
        this.isCollection = isCollection;
    }


    public boolean getIscollection() {
        return isCollection;
    }

    public void setIscollection(boolean isCollection) {
        this.isCollection = isCollection;
    }

    public classDiagram_Attribute getClassdiagram_attribute() {
        return classdiagram_attribute;
    }

    public void setClassdiagram_attribute(classDiagram_Attribute classdiagram_attribute) {
        this.classdiagram_attribute = classdiagram_attribute;
    }
    public classDiagram_Classifier getClassdiagram_classifier() {
        return classdiagram_classifier;
    }

    public void setClassdiagram_classifier(classDiagram_Classifier classdiagram_classifier) {
        this.classdiagram_classifier = classdiagram_classifier;
    }
    public classDiagram_Method getClassdiagram_method() {
        return classdiagram_method;
    }

    public void setClassdiagram_method(classDiagram_Method classdiagram_method) {
        this.classdiagram_method = classdiagram_method;
    }

}