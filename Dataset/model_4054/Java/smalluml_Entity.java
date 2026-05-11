





import java.util.List;
import java.util.ArrayList;

public class smalluml_Entity  {

    private String name;





    private smalluml_ClassDiagram smalluml_classdiagram;


    public smalluml_Entity(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public smalluml_ClassDiagram getSmalluml_classdiagram() {
        return smalluml_classdiagram;
    }

    public void setSmalluml_classdiagram(smalluml_ClassDiagram smalluml_classdiagram) {
        this.smalluml_classdiagram = smalluml_classdiagram;
    }

}