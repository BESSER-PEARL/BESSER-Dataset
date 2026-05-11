





import java.util.List;
import java.util.ArrayList;

public class classDiagram_Package extends ModelingConcept {






    private List<classDiagram_Class> classdiagram_classs;




    private classDiagram_ClassModel classdiagram_classmodel;




    private classDiagram_Package classdiagram_package;




    private List<classDiagram_Package> classdiagram_packages;


    public classDiagram_Package(
    ) {
        super(
        );
        this.classdiagram_classs = new ArrayList<>();
        this.classdiagram_packages = new ArrayList<>();
    }

    public classDiagram_Package(
        ArrayList<classDiagram_Class> classdiagram_classs,        ArrayList<classDiagram_Package> classdiagram_packages    ) {
        this.classdiagram_classs = classdiagram_classs;
        this.classdiagram_packages = classdiagram_packages;
    }


    public List<classDiagram_Class> getClassdiagram_classs() {
        return classdiagram_classs;
    }

    public void addClassdiagram_class(Classdiagram_class classdiagram_class) {
        this.classdiagram_classs.add(classdiagram_class);
    }
    public classDiagram_ClassModel getClassdiagram_classmodel() {
        return classdiagram_classmodel;
    }

    public void setClassdiagram_classmodel(classDiagram_ClassModel classdiagram_classmodel) {
        this.classdiagram_classmodel = classdiagram_classmodel;
    }
    public classDiagram_Package getClassdiagram_package() {
        return classdiagram_package;
    }

    public void setClassdiagram_package(classDiagram_Package classdiagram_package) {
        this.classdiagram_package = classdiagram_package;
    }
    public List<classDiagram_Package> getClassdiagram_packages() {
        return classdiagram_packages;
    }

    public void addClassdiagram_package(Classdiagram_package classdiagram_package) {
        this.classdiagram_packages.add(classdiagram_package);
    }

}