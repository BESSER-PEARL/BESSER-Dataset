





import java.util.List;
import java.util.ArrayList;

public class ClassesProv_Package extends PackageableElement, Namespace {

    private String URI;





    private List<ClassesProv_PackageMerge> classesprov_packagemerges;




    private ClassesProv_Type classesprov_type;




    private ClassesProv_PackageImport classesprov_packageimport;




    private ClassesProv_PackageMerge classesprov_packagemerge;




    private ClassesProv_PackageMerge classesprov_packagemerge;




    private List<ClassesProv_PackageableElement> classesprov_packageableelements;




    private ClassesProv_Package classesprov_package;




    private List<ClassesProv_Package> classesprov_packages;




    private List<ClassesProv_Type> classesprov_types;


    public ClassesProv_Package(
        String URI    ) {
        super(
        );
        this.URI = URI;
        this.classesprov_packagemerges = new ArrayList<>();
        this.classesprov_packageableelements = new ArrayList<>();
        this.classesprov_packages = new ArrayList<>();
        this.classesprov_types = new ArrayList<>();
    }

    public ClassesProv_Package(
        String URI        ArrayList<ClassesProv_PackageMerge> classesprov_packagemerges,        ArrayList<ClassesProv_PackageableElement> classesprov_packageableelements,        ArrayList<ClassesProv_Package> classesprov_packages,        ArrayList<ClassesProv_Type> classesprov_types    ) {
        this.URI = URI;
        this.classesprov_packagemerges = classesprov_packagemerges;
        this.classesprov_packageableelements = classesprov_packageableelements;
        this.classesprov_packages = classesprov_packages;
        this.classesprov_types = classesprov_types;
    }

    public String getUri() {
        return URI;
    }

    public void setUri(String URI) {
        this.URI = URI;
    }

    public List<ClassesProv_PackageMerge> getClassesprov_packagemerges() {
        return classesprov_packagemerges;
    }

    public void addClassesprov_packagemerge(Classesprov_packagemerge classesprov_packagemerge) {
        this.classesprov_packagemerges.add(classesprov_packagemerge);
    }
    public ClassesProv_Type getClassesprov_type() {
        return classesprov_type;
    }

    public void setClassesprov_type(ClassesProv_Type classesprov_type) {
        this.classesprov_type = classesprov_type;
    }
    public ClassesProv_PackageImport getClassesprov_packageimport() {
        return classesprov_packageimport;
    }

    public void setClassesprov_packageimport(ClassesProv_PackageImport classesprov_packageimport) {
        this.classesprov_packageimport = classesprov_packageimport;
    }
    public ClassesProv_PackageMerge getClassesprov_packagemerge() {
        return classesprov_packagemerge;
    }

    public void setClassesprov_packagemerge(ClassesProv_PackageMerge classesprov_packagemerge) {
        this.classesprov_packagemerge = classesprov_packagemerge;
    }
    public ClassesProv_PackageMerge getClassesprov_packagemerge() {
        return classesprov_packagemerge;
    }

    public void setClassesprov_packagemerge(ClassesProv_PackageMerge classesprov_packagemerge) {
        this.classesprov_packagemerge = classesprov_packagemerge;
    }
    public List<ClassesProv_PackageableElement> getClassesprov_packageableelements() {
        return classesprov_packageableelements;
    }

    public void addClassesprov_packageableelement(Classesprov_packageableelement classesprov_packageableelement) {
        this.classesprov_packageableelements.add(classesprov_packageableelement);
    }
    public ClassesProv_Package getClassesprov_package() {
        return classesprov_package;
    }

    public void setClassesprov_package(ClassesProv_Package classesprov_package) {
        this.classesprov_package = classesprov_package;
    }
    public List<ClassesProv_Package> getClassesprov_packages() {
        return classesprov_packages;
    }

    public void addClassesprov_package(Classesprov_package classesprov_package) {
        this.classesprov_packages.add(classesprov_package);
    }
    public List<ClassesProv_Type> getClassesprov_types() {
        return classesprov_types;
    }

    public void addClassesprov_type(Classesprov_type classesprov_type) {
        this.classesprov_types.add(classesprov_type);
    }

}