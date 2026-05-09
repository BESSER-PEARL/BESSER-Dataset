





import java.util.List;
import java.util.ArrayList;

public class javaDsl_PackageStatement  {

    private String name;





    private javaDsl_CompilationUnit javadsl_compilationunit;


    public javaDsl_PackageStatement(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public javaDsl_CompilationUnit getJavadsl_compilationunit() {
        return javadsl_compilationunit;
    }

    public void setJavadsl_compilationunit(javaDsl_CompilationUnit javadsl_compilationunit) {
        this.javadsl_compilationunit = javadsl_compilationunit;
    }

}