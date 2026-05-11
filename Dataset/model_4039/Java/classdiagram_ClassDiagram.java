





import java.util.List;
import java.util.ArrayList;

public class classdiagram_ClassDiagram  {






    private List<classdiagram_Class> classdiagram_classs;




    private List<classdiagram_Association> classdiagram_associations;




    private List<classdiagram_Dependency> classdiagram_dependencys;


    public classdiagram_ClassDiagram(
    ) {
        this.classdiagram_classs = new ArrayList<>();
        this.classdiagram_associations = new ArrayList<>();
        this.classdiagram_dependencys = new ArrayList<>();
    }

    public classdiagram_ClassDiagram(
        ArrayList<classdiagram_Class> classdiagram_classs,        ArrayList<classdiagram_Association> classdiagram_associations,        ArrayList<classdiagram_Dependency> classdiagram_dependencys    ) {
        this.classdiagram_classs = classdiagram_classs;
        this.classdiagram_associations = classdiagram_associations;
        this.classdiagram_dependencys = classdiagram_dependencys;
    }


    public List<classdiagram_Class> getClassdiagram_classs() {
        return classdiagram_classs;
    }

    public void addClassdiagram_class(Classdiagram_class classdiagram_class) {
        this.classdiagram_classs.add(classdiagram_class);
    }
    public List<classdiagram_Association> getClassdiagram_associations() {
        return classdiagram_associations;
    }

    public void addClassdiagram_association(Classdiagram_association classdiagram_association) {
        this.classdiagram_associations.add(classdiagram_association);
    }
    public List<classdiagram_Dependency> getClassdiagram_dependencys() {
        return classdiagram_dependencys;
    }

    public void addClassdiagram_dependency(Classdiagram_dependency classdiagram_dependency) {
        this.classdiagram_dependencys.add(classdiagram_dependency);
    }

}