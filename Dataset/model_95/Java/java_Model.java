





import java.util.List;
import java.util.ArrayList;

public class java_Model  {

    private String name;





    private List<java_Archive> java_archives;




    private List<java_CompilationUnit> java_compilationunits;




    private List<java_Type> java_types;




    private List<java_Package> java_packages;


    public java_Model(
        String name    ) {
        this.name = name;
        this.java_archives = new ArrayList<>();
        this.java_compilationunits = new ArrayList<>();
        this.java_types = new ArrayList<>();
        this.java_packages = new ArrayList<>();
    }

    public java_Model(
        String name        ArrayList<java_Archive> java_archives,        ArrayList<java_CompilationUnit> java_compilationunits,        ArrayList<java_Type> java_types,        ArrayList<java_Package> java_packages    ) {
        this.name = name;
        this.java_archives = java_archives;
        this.java_compilationunits = java_compilationunits;
        this.java_types = java_types;
        this.java_packages = java_packages;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<java_Archive> getJava_archives() {
        return java_archives;
    }

    public void addJava_archive(Java_archive java_archive) {
        this.java_archives.add(java_archive);
    }
    public List<java_CompilationUnit> getJava_compilationunits() {
        return java_compilationunits;
    }

    public void addJava_compilationunit(Java_compilationunit java_compilationunit) {
        this.java_compilationunits.add(java_compilationunit);
    }
    public List<java_Type> getJava_types() {
        return java_types;
    }

    public void addJava_type(Java_type java_type) {
        this.java_types.add(java_type);
    }
    public List<java_Package> getJava_packages() {
        return java_packages;
    }

    public void addJava_package(Java_package java_package) {
        this.java_packages.add(java_package);
    }

}