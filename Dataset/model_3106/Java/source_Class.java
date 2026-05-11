





import java.util.List;
import java.util.ArrayList;

public class source_Class  {

    private String name;





    private source_ClassDiagram source_classdiagram;




    private source_Class source_class;


    public source_Class(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public source_ClassDiagram getSource_classdiagram() {
        return source_classdiagram;
    }

    public void setSource_classdiagram(source_ClassDiagram source_classdiagram) {
        this.source_classdiagram = source_classdiagram;
    }
    public source_Class getSource_class() {
        return source_class;
    }

    public void setSource_class(source_Class source_class) {
        this.source_class = source_class;
    }

}