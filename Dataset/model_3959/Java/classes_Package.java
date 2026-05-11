





import java.util.List;
import java.util.ArrayList;

public class classes_Package extends PackageableElement, Namespace {






    private classes_Package classes_package;




    private List<classes_Type> classes_types;




    private classes_Package classes_package;




    private classes_Type classes_type;




    private classes_PackageImport classes_packageimport;




    private List<classes_PackageableElement> classes_packageableelements;


    public classes_Package(
    ) {
        super(
        );
        this.classes_types = new ArrayList<>();
        this.classes_packageableelements = new ArrayList<>();
    }

    public classes_Package(
        ArrayList<classes_Type> classes_types,        ArrayList<classes_PackageableElement> classes_packageableelements    ) {
        this.classes_types = classes_types;
        this.classes_packageableelements = classes_packageableelements;
    }


    public classes_Package getClasses_package() {
        return classes_package;
    }

    public void setClasses_package(classes_Package classes_package) {
        this.classes_package = classes_package;
    }
    public List<classes_Type> getClasses_types() {
        return classes_types;
    }

    public void addClasses_type(Classes_type classes_type) {
        this.classes_types.add(classes_type);
    }
    public classes_Package getClasses_package() {
        return classes_package;
    }

    public void setClasses_package(classes_Package classes_package) {
        this.classes_package = classes_package;
    }
    public classes_Type getClasses_type() {
        return classes_type;
    }

    public void setClasses_type(classes_Type classes_type) {
        this.classes_type = classes_type;
    }
    public classes_PackageImport getClasses_packageimport() {
        return classes_packageimport;
    }

    public void setClasses_packageimport(classes_PackageImport classes_packageimport) {
        this.classes_packageimport = classes_packageimport;
    }
    public List<classes_PackageableElement> getClasses_packageableelements() {
        return classes_packageableelements;
    }

    public void addClasses_packageableelement(Classes_packageableelement classes_packageableelement) {
        this.classes_packageableelements.add(classes_packageableelement);
    }

}