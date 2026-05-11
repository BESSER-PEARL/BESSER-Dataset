





import java.util.List;
import java.util.ArrayList;

public class classDiagram_Attribute extends ModelingConcept {

    private String accessModifier;
    private boolean isStatic;



    public classDiagram_Attribute(
        String accessModifier,        boolean isStatic    ) {
        super(
        );
        this.accessModifier = accessModifier;
        this.isStatic = isStatic;
    }


    public String getAccessmodifier() {
        return accessModifier;
    }

    public void setAccessmodifier(String accessModifier) {
        this.accessModifier = accessModifier;
    }
    public boolean getIsstatic() {
        return isStatic;
    }

    public void setIsstatic(boolean isStatic) {
        this.isStatic = isStatic;
    }


}