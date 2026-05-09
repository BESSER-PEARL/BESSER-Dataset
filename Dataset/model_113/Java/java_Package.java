





import java.util.List;
import java.util.ArrayList;

public class java_Package extends JavaRoot, Annotable {






    private List<java_CompilationUnit> java_compilationunits;


    public java_Package(
    ) {
        super(
        );
        this.java_compilationunits = new ArrayList<>();
    }

    public java_Package(
        ArrayList<java_CompilationUnit> java_compilationunits    ) {
        this.java_compilationunits = java_compilationunits;
    }


    public List<java_CompilationUnit> getJava_compilationunits() {
        return java_compilationunits;
    }

    public void addJava_compilationunit(Java_compilationunit java_compilationunit) {
        this.java_compilationunits.add(java_compilationunit);
    }

}