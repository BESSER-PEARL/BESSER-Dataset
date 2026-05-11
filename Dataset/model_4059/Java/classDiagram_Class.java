





import java.util.List;
import java.util.ArrayList;

public class classDiagram_Class extends Classifier {

    private boolean isStatic;
    private String accessModifier;
    private boolean isAbstract;





    private classDiagram_Class classdiagram_class;




    private classDiagram_Class classdiagram_class;




    private List<classDiagram_Attribute> classdiagram_attributes;




    private List<classDiagram_Function> classdiagram_functions;


    public classDiagram_Class(
        boolean isStatic,        String accessModifier,        boolean isAbstract    ) {
        super(
        );
        this.isStatic = isStatic;
        this.accessModifier = accessModifier;
        this.isAbstract = isAbstract;
        this.classdiagram_attributes = new ArrayList<>();
        this.classdiagram_functions = new ArrayList<>();
    }

    public classDiagram_Class(
        boolean isStatic,        String accessModifier,        boolean isAbstract        ArrayList<classDiagram_Attribute> classdiagram_attributes,        ArrayList<classDiagram_Function> classdiagram_functions    ) {
        this.isStatic = isStatic;
        this.accessModifier = accessModifier;
        this.isAbstract = isAbstract;
        this.classdiagram_attributes = classdiagram_attributes;
        this.classdiagram_functions = classdiagram_functions;
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

    public classDiagram_Class getClassdiagram_class() {
        return classdiagram_class;
    }

    public void setClassdiagram_class(classDiagram_Class classdiagram_class) {
        this.classdiagram_class = classdiagram_class;
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
    public List<classDiagram_Function> getClassdiagram_functions() {
        return classdiagram_functions;
    }

    public void addClassdiagram_function(Classdiagram_function classdiagram_function) {
        this.classdiagram_functions.add(classdiagram_function);
    }

}