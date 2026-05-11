





import java.util.List;
import java.util.ArrayList;

public class classdiagram_Attribute  {

    private String name;





    private classdiagram_Class classdiagram_class;




    private classdiagram_ClassDiagram classdiagram_classdiagram;


    public classdiagram_Attribute(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public classdiagram_Class getClassdiagram_class() {
        return classdiagram_class;
    }

    public void setClassdiagram_class(classdiagram_Class classdiagram_class) {
        this.classdiagram_class = classdiagram_class;
    }
    public classdiagram_ClassDiagram getClassdiagram_classdiagram() {
        return classdiagram_classdiagram;
    }

    public void setClassdiagram_classdiagram(classdiagram_ClassDiagram classdiagram_classdiagram) {
        this.classdiagram_classdiagram = classdiagram_classdiagram;
    }

}