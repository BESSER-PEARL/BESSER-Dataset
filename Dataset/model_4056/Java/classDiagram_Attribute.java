





import java.util.List;
import java.util.ArrayList;

public class classDiagram_Attribute extends ModelingConcept {

    private boolean isStatic;
    private String accessModifier;





    private classDiagram_Class classdiagram_class;


    public classDiagram_Attribute(
        boolean isStatic,        String accessModifier    ) {
        super(
        );
        this.isStatic = isStatic;
        this.accessModifier = accessModifier;
    }


    public boolean getIsstatic() {
        return isStatic;
    }

    public void setIsstatic(boolean isStatic) {
        this.isStatic = isStatic;
    }
    public String getAccessmodifier() {
        return accessModifier;
    }

    public void setAccessmodifier(String accessModifier) {
        this.accessModifier = accessModifier;
    }

    public classDiagram_Class getClassdiagram_class() {
        return classdiagram_class;
    }

    public void setClassdiagram_class(classDiagram_Class classdiagram_class) {
        this.classdiagram_class = classdiagram_class;
    }

}