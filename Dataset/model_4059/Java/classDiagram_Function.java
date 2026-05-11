





import java.util.List;
import java.util.ArrayList;

public class classDiagram_Function extends ModelingConcept {

    private String body;
    private boolean isAbstract;
    private String accessModifier;
    private boolean isStatic;





    private List<classDiagram_Attribute> classdiagram_attributes;


    public classDiagram_Function(
        String body,        boolean isAbstract,        String accessModifier,        boolean isStatic    ) {
        super(
        );
        this.body = body;
        this.isAbstract = isAbstract;
        this.accessModifier = accessModifier;
        this.isStatic = isStatic;
        this.classdiagram_attributes = new ArrayList<>();
    }

    public classDiagram_Function(
        String body,        boolean isAbstract,        String accessModifier,        boolean isStatic        ArrayList<classDiagram_Attribute> classdiagram_attributes    ) {
        this.body = body;
        this.isAbstract = isAbstract;
        this.accessModifier = accessModifier;
        this.isStatic = isStatic;
        this.classdiagram_attributes = classdiagram_attributes;
    }

    public String getBody() {
        return body;
    }

    public void setBody(String body) {
        this.body = body;
    }
    public boolean getIsabstract() {
        return isAbstract;
    }

    public void setIsabstract(boolean isAbstract) {
        this.isAbstract = isAbstract;
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

    public List<classDiagram_Attribute> getClassdiagram_attributes() {
        return classdiagram_attributes;
    }

    public void addClassdiagram_attribute(Classdiagram_attribute classdiagram_attribute) {
        this.classdiagram_attributes.add(classdiagram_attribute);
    }

}