





import java.util.List;
import java.util.ArrayList;

public class ClassesProv_Dependency extends PackageableElement, DirectedRelationship {






    private List<ClassesProv_NamedElement> classesprov_namedelements;




    private ClassesProv_NamedElement classesprov_namedelement;




    private List<ClassesProv_NamedElement> classesprov_namedelements;


    public ClassesProv_Dependency(
    ) {
        super(
        );
        this.classesprov_namedelements = new ArrayList<>();
        this.classesprov_namedelements = new ArrayList<>();
    }

    public ClassesProv_Dependency(
        ArrayList<ClassesProv_NamedElement> classesprov_namedelements,        ArrayList<ClassesProv_NamedElement> classesprov_namedelements    ) {
        this.classesprov_namedelements = classesprov_namedelements;
        this.classesprov_namedelements = classesprov_namedelements;
    }


    public List<ClassesProv_NamedElement> getClassesprov_namedelements() {
        return classesprov_namedelements;
    }

    public void addClassesprov_namedelement(Classesprov_namedelement classesprov_namedelement) {
        this.classesprov_namedelements.add(classesprov_namedelement);
    }
    public ClassesProv_NamedElement getClassesprov_namedelement() {
        return classesprov_namedelement;
    }

    public void setClassesprov_namedelement(ClassesProv_NamedElement classesprov_namedelement) {
        this.classesprov_namedelement = classesprov_namedelement;
    }
    public List<ClassesProv_NamedElement> getClassesprov_namedelements() {
        return classesprov_namedelements;
    }

    public void addClassesprov_namedelement(Classesprov_namedelement classesprov_namedelement) {
        this.classesprov_namedelements.add(classesprov_namedelement);
    }

}