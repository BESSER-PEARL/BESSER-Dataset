





import java.util.List;
import java.util.ArrayList;

public class source_Association  {

    private String name;
    private int leftMultiplicity;





    private source_Class source_class;




    private source_ClassDiagram source_classdiagram;




    private source_Class source_class;


    public source_Association(
        String name,        int leftMultiplicity    ) {
        this.name = name;
        this.leftMultiplicity = leftMultiplicity;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getLeftmultiplicity() {
        return leftMultiplicity;
    }

    public void setLeftmultiplicity(int leftMultiplicity) {
        this.leftMultiplicity = leftMultiplicity;
    }

    public source_Class getSource_class() {
        return source_class;
    }

    public void setSource_class(source_Class source_class) {
        this.source_class = source_class;
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