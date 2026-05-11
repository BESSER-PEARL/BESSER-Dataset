





import java.util.List;
import java.util.ArrayList;

public class classdiagram_Class extends NamedElement {






    private classdiagram_Dependency classdiagram_dependency;




    private List<classdiagram_Dependency> classdiagram_dependencys;




    private classdiagram_Association classdiagram_association;




    private classdiagram_Dependency classdiagram_dependency;




    private List<classdiagram_Association> classdiagram_associations;




    private List<classdiagram_Association> classdiagram_associations;




    private List<classdiagram_Dependency> classdiagram_dependencys;




    private classdiagram_Class classdiagram_class;




    private List<classdiagram_Class> classdiagram_classs;




    private classdiagram_Association classdiagram_association;




    private classdiagram_Class classdiagram_class;




    private classdiagram_Class classdiagram_class;


    public classdiagram_Class(
    ) {
        super(
        );
        this.classdiagram_dependencys = new ArrayList<>();
        this.classdiagram_associations = new ArrayList<>();
        this.classdiagram_associations = new ArrayList<>();
        this.classdiagram_dependencys = new ArrayList<>();
        this.classdiagram_classs = new ArrayList<>();
    }

    public classdiagram_Class(
        ArrayList<classdiagram_Dependency> classdiagram_dependencys,        ArrayList<classdiagram_Association> classdiagram_associations,        ArrayList<classdiagram_Association> classdiagram_associations,        ArrayList<classdiagram_Dependency> classdiagram_dependencys,        ArrayList<classdiagram_Class> classdiagram_classs    ) {
        this.classdiagram_dependencys = classdiagram_dependencys;
        this.classdiagram_associations = classdiagram_associations;
        this.classdiagram_associations = classdiagram_associations;
        this.classdiagram_dependencys = classdiagram_dependencys;
        this.classdiagram_classs = classdiagram_classs;
    }


    public classdiagram_Dependency getClassdiagram_dependency() {
        return classdiagram_dependency;
    }

    public void setClassdiagram_dependency(classdiagram_Dependency classdiagram_dependency) {
        this.classdiagram_dependency = classdiagram_dependency;
    }
    public List<classdiagram_Dependency> getClassdiagram_dependencys() {
        return classdiagram_dependencys;
    }

    public void addClassdiagram_dependency(Classdiagram_dependency classdiagram_dependency) {
        this.classdiagram_dependencys.add(classdiagram_dependency);
    }
    public classdiagram_Association getClassdiagram_association() {
        return classdiagram_association;
    }

    public void setClassdiagram_association(classdiagram_Association classdiagram_association) {
        this.classdiagram_association = classdiagram_association;
    }
    public classdiagram_Dependency getClassdiagram_dependency() {
        return classdiagram_dependency;
    }

    public void setClassdiagram_dependency(classdiagram_Dependency classdiagram_dependency) {
        this.classdiagram_dependency = classdiagram_dependency;
    }
    public List<classdiagram_Association> getClassdiagram_associations() {
        return classdiagram_associations;
    }

    public void addClassdiagram_association(Classdiagram_association classdiagram_association) {
        this.classdiagram_associations.add(classdiagram_association);
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
    public classdiagram_Class getClassdiagram_class() {
        return classdiagram_class;
    }

    public void setClassdiagram_class(classdiagram_Class classdiagram_class) {
        this.classdiagram_class = classdiagram_class;
    }
    public List<classdiagram_Class> getClassdiagram_classs() {
        return classdiagram_classs;
    }

    public void addClassdiagram_class(Classdiagram_class classdiagram_class) {
        this.classdiagram_classs.add(classdiagram_class);
    }
    public classdiagram_Association getClassdiagram_association() {
        return classdiagram_association;
    }

    public void setClassdiagram_association(classdiagram_Association classdiagram_association) {
        this.classdiagram_association = classdiagram_association;
    }
    public classdiagram_Class getClassdiagram_class() {
        return classdiagram_class;
    }

    public void setClassdiagram_class(classdiagram_Class classdiagram_class) {
        this.classdiagram_class = classdiagram_class;
    }
    public classdiagram_Class getClassdiagram_class() {
        return classdiagram_class;
    }

    public void setClassdiagram_class(classdiagram_Class classdiagram_class) {
        this.classdiagram_class = classdiagram_class;
    }

}