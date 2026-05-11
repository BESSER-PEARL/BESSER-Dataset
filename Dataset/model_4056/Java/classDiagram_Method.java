





import java.util.List;
import java.util.ArrayList;

public class classDiagram_Method extends ModelingConcept {

    private boolean isStatic;
    private String accessModifier;
    private boolean isAbstract;
    private String body;





    private classDiagram_Class classdiagram_class;




    private List<classDiagram_Attribute> classdiagram_attributes;


    public classDiagram_Method(
        boolean isStatic,        String accessModifier,        boolean isAbstract,        String body    ) {
        super(
        );
        this.isStatic = isStatic;
        this.accessModifier = accessModifier;
        this.isAbstract = isAbstract;
        this.body = body;
        this.classdiagram_attributes = new ArrayList<>();
    }

    public classDiagram_Method(
        boolean isStatic,        String accessModifier,        boolean isAbstract,        String body        ArrayList<classDiagram_Attribute> classdiagram_attributes    ) {
        this.isStatic = isStatic;
        this.accessModifier = accessModifier;
        this.isAbstract = isAbstract;
        this.body = body;
        this.classdiagram_attributes = classdiagram_attributes;
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
    public boolean getIsabstract() {
        return isAbstract;
    }

    public void setIsabstract(boolean isAbstract) {
        this.isAbstract = isAbstract;
    }
    public String getBody() {
        return body;
    }

    public void setBody(String body) {
        this.body = body;
    }

    public classDiagram_Class getClassdiagram_class() {
        return classdiagram_class;
    }

    public void setClassdiagram_class(classDiagram_Class classdiagram_class) {
        this.classdiagram_class = classdiagram_class;
    }
    public List<classDiagram_Attribute> getClassdiagram_attributes() {
        return classdiagram_attributes;
    }

    public void addClassdiagram_attribute(Classdiagram_attribute classdiagram_attribute) {
        this.classdiagram_attributes.add(classdiagram_attribute);
    }

}