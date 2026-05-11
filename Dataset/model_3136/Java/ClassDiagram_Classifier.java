





import java.util.List;
import java.util.ArrayList;

public class ClassDiagram_Classifier  {

    private String name;





    private ClassDiagram_Generalization classdiagram_generalization;




    private ClassDiagram_Dependency classdiagram_dependency;




    private ClassDiagram_Dependency classdiagram_dependency;




    private ClassDiagram_Generalization classdiagram_generalization;


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

    public ClassDiagram_Generalization getClassdiagram_generalization() {
        return classdiagram_generalization;
    }

    public void setClassdiagram_generalization(ClassDiagram_Generalization classdiagram_generalization) {
        this.classdiagram_generalization = classdiagram_generalization;
    }
    public ClassDiagram_Dependency getClassdiagram_dependency() {
        return classdiagram_dependency;
    }

    public void setClassdiagram_dependency(ClassDiagram_Dependency classdiagram_dependency) {
        this.classdiagram_dependency = classdiagram_dependency;
    }
    public ClassDiagram_Dependency getClassdiagram_dependency() {
        return classdiagram_dependency;
    }

    public void setClassdiagram_dependency(ClassDiagram_Dependency classdiagram_dependency) {
        this.classdiagram_dependency = classdiagram_dependency;
    }
    public ClassDiagram_Generalization getClassdiagram_generalization() {
        return classdiagram_generalization;
    }

    public void setClassdiagram_generalization(ClassDiagram_Generalization classdiagram_generalization) {
        this.classdiagram_generalization = classdiagram_generalization;
    }

}