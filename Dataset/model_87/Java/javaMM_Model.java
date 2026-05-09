





import java.util.List;
import java.util.ArrayList;

public class javaMM_Model  {

    private String name;





    private List<javaMM_Type> javamm_types;




    private List<javaMM_ClassFile> javamm_classfiles;




    private List<javaMM_Package> javamm_packages;




    private List<javaMM_CompilationUnit> javamm_compilationunits;




    private List<javaMM_UnresolvedItem> javamm_unresolveditems;




    private List<javaMM_Archive> javamm_archives;




    private javaMM_Package javamm_package;


    public javaMM_Model(
        String name    ) {
        this.name = name;
        this.javamm_types = new ArrayList<>();
        this.javamm_classfiles = new ArrayList<>();
        this.javamm_packages = new ArrayList<>();
        this.javamm_compilationunits = new ArrayList<>();
        this.javamm_unresolveditems = new ArrayList<>();
        this.javamm_archives = new ArrayList<>();
    }

    public javaMM_Model(
        String name        ArrayList<javaMM_Type> javamm_types,        ArrayList<javaMM_ClassFile> javamm_classfiles,        ArrayList<javaMM_Package> javamm_packages,        ArrayList<javaMM_CompilationUnit> javamm_compilationunits,        ArrayList<javaMM_UnresolvedItem> javamm_unresolveditems,        ArrayList<javaMM_Archive> javamm_archives    ) {
        this.name = name;
        this.javamm_types = javamm_types;
        this.javamm_classfiles = javamm_classfiles;
        this.javamm_packages = javamm_packages;
        this.javamm_compilationunits = javamm_compilationunits;
        this.javamm_unresolveditems = javamm_unresolveditems;
        this.javamm_archives = javamm_archives;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<javaMM_Type> getJavamm_types() {
        return javamm_types;
    }

    public void addJavamm_type(Javamm_type javamm_type) {
        this.javamm_types.add(javamm_type);
    }
    public List<javaMM_ClassFile> getJavamm_classfiles() {
        return javamm_classfiles;
    }

    public void addJavamm_classfile(Javamm_classfile javamm_classfile) {
        this.javamm_classfiles.add(javamm_classfile);
    }
    public List<javaMM_Package> getJavamm_packages() {
        return javamm_packages;
    }

    public void addJavamm_package(Javamm_package javamm_package) {
        this.javamm_packages.add(javamm_package);
    }
    public List<javaMM_CompilationUnit> getJavamm_compilationunits() {
        return javamm_compilationunits;
    }

    public void addJavamm_compilationunit(Javamm_compilationunit javamm_compilationunit) {
        this.javamm_compilationunits.add(javamm_compilationunit);
    }
    public List<javaMM_UnresolvedItem> getJavamm_unresolveditems() {
        return javamm_unresolveditems;
    }

    public void addJavamm_unresolveditem(Javamm_unresolveditem javamm_unresolveditem) {
        this.javamm_unresolveditems.add(javamm_unresolveditem);
    }
    public List<javaMM_Archive> getJavamm_archives() {
        return javamm_archives;
    }

    public void addJavamm_archive(Javamm_archive javamm_archive) {
        this.javamm_archives.add(javamm_archive);
    }
    public javaMM_Package getJavamm_package() {
        return javamm_package;
    }

    public void setJavamm_package(javaMM_Package javamm_package) {
        this.javamm_package = javamm_package;
    }

}