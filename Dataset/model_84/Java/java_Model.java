





import java.util.List;
import java.util.ArrayList;

public class java_Model  {

    private String name;





    private List<java_CompilationUnit> java_compilationunits;


    public java_Model(
        String name    ) {
        this.name = name;
        this.java_compilationunits = new ArrayList<>();
    }

    public java_Model(
        String name        ArrayList<java_CompilationUnit> java_compilationunits    ) {
        this.name = name;
        this.java_compilationunits = java_compilationunits;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<java_CompilationUnit> getJava_compilationunits() {
        return java_compilationunits;
    }

    public void addJava_compilationunit(Java_compilationunit java_compilationunit) {
        this.java_compilationunits.add(java_compilationunit);
    }

}