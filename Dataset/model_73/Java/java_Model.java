





import java.util.List;
import java.util.ArrayList;

public class java_Model  {

    private String name;





    private List<java_ClassFile> java_classfiles;




    private List<java_Archive> java_archives;




    private List<java_Package> java_packages;




    private List<java_UnresolvedItem> java_unresolveditems;




    private List<java_Type> java_types;




    private List<java_CompilationUnit> java_compilationunits;




    private java_Package java_package;


    public java_Model(
        String name    ) {
        this.name = name;
        this.java_classfiles = new ArrayList<>();
        this.java_archives = new ArrayList<>();
        this.java_packages = new ArrayList<>();
        this.java_unresolveditems = new ArrayList<>();
        this.java_types = new ArrayList<>();
        this.java_compilationunits = new ArrayList<>();
    }

    public java_Model(
        String name        ArrayList<java_ClassFile> java_classfiles,        ArrayList<java_Archive> java_archives,        ArrayList<java_Package> java_packages,        ArrayList<java_UnresolvedItem> java_unresolveditems,        ArrayList<java_Type> java_types,        ArrayList<java_CompilationUnit> java_compilationunits    ) {
        this.name = name;
        this.java_classfiles = java_classfiles;
        this.java_archives = java_archives;
        this.java_packages = java_packages;
        this.java_unresolveditems = java_unresolveditems;
        this.java_types = java_types;
        this.java_compilationunits = java_compilationunits;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<java_ClassFile> getJava_classfiles() {
        return java_classfiles;
    }

    public void addJava_classfile(Java_classfile java_classfile) {
        this.java_classfiles.add(java_classfile);
    }
    public List<java_Archive> getJava_archives() {
        return java_archives;
    }

    public void addJava_archive(Java_archive java_archive) {
        this.java_archives.add(java_archive);
    }
    public List<java_Package> getJava_packages() {
        return java_packages;
    }

    public void addJava_package(Java_package java_package) {
        this.java_packages.add(java_package);
    }
    public List<java_UnresolvedItem> getJava_unresolveditems() {
        return java_unresolveditems;
    }

    public void addJava_unresolveditem(Java_unresolveditem java_unresolveditem) {
        this.java_unresolveditems.add(java_unresolveditem);
    }
    public List<java_Type> getJava_types() {
        return java_types;
    }

    public void addJava_type(Java_type java_type) {
        this.java_types.add(java_type);
    }
    public List<java_CompilationUnit> getJava_compilationunits() {
        return java_compilationunits;
    }

    public void addJava_compilationunit(Java_compilationunit java_compilationunit) {
        this.java_compilationunits.add(java_compilationunit);
    }
    public java_Package getJava_package() {
        return java_package;
    }

    public void setJava_package(java_Package java_package) {
        this.java_package = java_package;
    }

}