





import java.util.List;
import java.util.ArrayList;

public class Java_Model  {

    private String name;





    private List<Java_Archive> java_archives;




    private List<Java_Type> java_types;




    private List<Java_CompilationUnit> java_compilationunits;




    private List<Java_Package> java_packages;




    private List<Java_ClassFile> java_classfiles;




    private Java_Package java_package;




    private List<Java_UnresolvedItem> java_unresolveditems;


    public Java_Model(
        String name    ) {
        this.name = name;
        this.java_archives = new ArrayList<>();
        this.java_types = new ArrayList<>();
        this.java_compilationunits = new ArrayList<>();
        this.java_packages = new ArrayList<>();
        this.java_classfiles = new ArrayList<>();
        this.java_unresolveditems = new ArrayList<>();
    }

    public Java_Model(
        String name        ArrayList<Java_Archive> java_archives,        ArrayList<Java_Type> java_types,        ArrayList<Java_CompilationUnit> java_compilationunits,        ArrayList<Java_Package> java_packages,        ArrayList<Java_ClassFile> java_classfiles,        ArrayList<Java_UnresolvedItem> java_unresolveditems    ) {
        this.name = name;
        this.java_archives = java_archives;
        this.java_types = java_types;
        this.java_compilationunits = java_compilationunits;
        this.java_packages = java_packages;
        this.java_classfiles = java_classfiles;
        this.java_unresolveditems = java_unresolveditems;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<Java_Archive> getJava_archives() {
        return java_archives;
    }

    public void addJava_archive(Java_archive java_archive) {
        this.java_archives.add(java_archive);
    }
    public List<Java_Type> getJava_types() {
        return java_types;
    }

    public void addJava_type(Java_type java_type) {
        this.java_types.add(java_type);
    }
    public List<Java_CompilationUnit> getJava_compilationunits() {
        return java_compilationunits;
    }

    public void addJava_compilationunit(Java_compilationunit java_compilationunit) {
        this.java_compilationunits.add(java_compilationunit);
    }
    public List<Java_Package> getJava_packages() {
        return java_packages;
    }

    public void addJava_package(Java_package java_package) {
        this.java_packages.add(java_package);
    }
    public List<Java_ClassFile> getJava_classfiles() {
        return java_classfiles;
    }

    public void addJava_classfile(Java_classfile java_classfile) {
        this.java_classfiles.add(java_classfile);
    }
    public Java_Package getJava_package() {
        return java_package;
    }

    public void setJava_package(Java_Package java_package) {
        this.java_package = java_package;
    }
    public List<Java_UnresolvedItem> getJava_unresolveditems() {
        return java_unresolveditems;
    }

    public void addJava_unresolveditem(Java_unresolveditem java_unresolveditem) {
        this.java_unresolveditems.add(java_unresolveditem);
    }

}