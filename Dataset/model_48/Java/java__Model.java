





import java.util.List;
import java.util.ArrayList;

public class java__Model  {

    private String name;





    private java__Package java__package;




    private List<java__Archive> java__archives;




    private List<java__CompilationUnit> java__compilationunits;




    private List<java__UnresolvedItem> java__unresolveditems;




    private List<java__ClassFile> java__classfiles;




    private List<java__Type> java__types;




    private List<java__Package> java__packages;


    public java__Model(
        String name    ) {
        this.name = name;
        this.java__archives = new ArrayList<>();
        this.java__compilationunits = new ArrayList<>();
        this.java__unresolveditems = new ArrayList<>();
        this.java__classfiles = new ArrayList<>();
        this.java__types = new ArrayList<>();
        this.java__packages = new ArrayList<>();
    }

    public java__Model(
        String name        ArrayList<java__Archive> java__archives,        ArrayList<java__CompilationUnit> java__compilationunits,        ArrayList<java__UnresolvedItem> java__unresolveditems,        ArrayList<java__ClassFile> java__classfiles,        ArrayList<java__Type> java__types,        ArrayList<java__Package> java__packages    ) {
        this.name = name;
        this.java__archives = java__archives;
        this.java__compilationunits = java__compilationunits;
        this.java__unresolveditems = java__unresolveditems;
        this.java__classfiles = java__classfiles;
        this.java__types = java__types;
        this.java__packages = java__packages;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public java__Package getJava__package() {
        return java__package;
    }

    public void setJava__package(java__Package java__package) {
        this.java__package = java__package;
    }
    public List<java__Archive> getJava__archives() {
        return java__archives;
    }

    public void addJava__archive(Java__archive java__archive) {
        this.java__archives.add(java__archive);
    }
    public List<java__CompilationUnit> getJava__compilationunits() {
        return java__compilationunits;
    }

    public void addJava__compilationunit(Java__compilationunit java__compilationunit) {
        this.java__compilationunits.add(java__compilationunit);
    }
    public List<java__UnresolvedItem> getJava__unresolveditems() {
        return java__unresolveditems;
    }

    public void addJava__unresolveditem(Java__unresolveditem java__unresolveditem) {
        this.java__unresolveditems.add(java__unresolveditem);
    }
    public List<java__ClassFile> getJava__classfiles() {
        return java__classfiles;
    }

    public void addJava__classfile(Java__classfile java__classfile) {
        this.java__classfiles.add(java__classfile);
    }
    public List<java__Type> getJava__types() {
        return java__types;
    }

    public void addJava__type(Java__type java__type) {
        this.java__types.add(java__type);
    }
    public List<java__Package> getJava__packages() {
        return java__packages;
    }

    public void addJava__package(Java__package java__package) {
        this.java__packages.add(java__package);
    }

}