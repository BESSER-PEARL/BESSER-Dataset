





import java.util.List;
import java.util.ArrayList;

public class Java5_Model  {

    private String name;





    private List<Java5_CompilationUnit> java5_compilationunits;


    public Java5_Model(
        String name    ) {
        this.name = name;
        this.java5_compilationunits = new ArrayList<>();
    }

    public Java5_Model(
        String name        ArrayList<Java5_CompilationUnit> java5_compilationunits    ) {
        this.name = name;
        this.java5_compilationunits = java5_compilationunits;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<Java5_CompilationUnit> getJava5_compilationunits() {
        return java5_compilationunits;
    }

    public void addJava5_compilationunit(Java5_compilationunit java5_compilationunit) {
        this.java5_compilationunits.add(java5_compilationunit);
    }

}