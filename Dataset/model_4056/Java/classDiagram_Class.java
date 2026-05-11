





import java.util.List;
import java.util.ArrayList;

public class classDiagram_Class extends Classifier {

    private boolean isAbstract;
    private String accessModifier;
    private boolean isStatic;





    private List<classDiagram_Class> classdiagram_classs;




    private classDiagram_Class classdiagram_class;


    public classDiagram_Class(
        boolean isAbstract,        String accessModifier,        boolean isStatic    ) {
        super(
        );
        this.isAbstract = isAbstract;
        this.accessModifier = accessModifier;
        this.isStatic = isStatic;
        this.classdiagram_classs = new ArrayList<>();
    }

    public classDiagram_Class(
        boolean isAbstract,        String accessModifier,        boolean isStatic        ArrayList<classDiagram_Class> classdiagram_classs    ) {
        this.isAbstract = isAbstract;
        this.accessModifier = accessModifier;
        this.isStatic = isStatic;
        this.classdiagram_classs = classdiagram_classs;
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

    public List<classDiagram_Class> getClassdiagram_classs() {
        return classdiagram_classs;
    }

    public void addClassdiagram_class(Classdiagram_class classdiagram_class) {
        this.classdiagram_classs.add(classdiagram_class);
    }
    public classDiagram_Class getClassdiagram_class() {
        return classdiagram_class;
    }

    public void setClassdiagram_class(classDiagram_Class classdiagram_class) {
        this.classdiagram_class = classdiagram_class;
    }

}