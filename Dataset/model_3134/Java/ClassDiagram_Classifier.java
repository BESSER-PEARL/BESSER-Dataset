





import java.util.List;
import java.util.ArrayList;

public class ClassDiagram_Classifier  {

    private String name;





    private ClassDiagram_TypedElement classdiagram_typedelement;




    private ClassDiagram_Model classdiagram_model;


    public ClassDiagram_Classifier(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public ClassDiagram_TypedElement getClassdiagram_typedelement() {
        return classdiagram_typedelement;
    }

    public void setClassdiagram_typedelement(ClassDiagram_TypedElement classdiagram_typedelement) {
        this.classdiagram_typedelement = classdiagram_typedelement;
    }
    public ClassDiagram_Model getClassdiagram_model() {
        return classdiagram_model;
    }

    public void setClassdiagram_model(ClassDiagram_Model classdiagram_model) {
        this.classdiagram_model = classdiagram_model;
    }

}