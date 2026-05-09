





import java.util.List;
import java.util.ArrayList;

public class javaDsl_ImportStatement  {

    private String object;
    private String package;





    private javaDsl_CompilationUnit javadsl_compilationunit;


    public javaDsl_ImportStatement(
        String object,        String package    ) {
        this.object = object;
        this.package = package;
    }


    public String getObject() {
        return object;
    }

    public void setObject(String object) {
        this.object = object;
    }
    public String getPackage() {
        return package;
    }

    public void setPackage(String package) {
        this.package = package;
    }

    public javaDsl_CompilationUnit getJavadsl_compilationunit() {
        return javadsl_compilationunit;
    }

    public void setJavadsl_compilationunit(javaDsl_CompilationUnit javadsl_compilationunit) {
        this.javadsl_compilationunit = javadsl_compilationunit;
    }

}