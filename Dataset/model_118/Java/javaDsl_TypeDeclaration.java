





import java.util.List;
import java.util.ArrayList;

public class javaDsl_TypeDeclaration  {

    private String doc;





    private javaDsl_CompilationUnit javadsl_compilationunit;


    public javaDsl_TypeDeclaration(
        String doc    ) {
        this.doc = doc;
    }


    public String getDoc() {
        return doc;
    }

    public void setDoc(String doc) {
        this.doc = doc;
    }

    public javaDsl_CompilationUnit getJavadsl_compilationunit() {
        return javadsl_compilationunit;
    }

    public void setJavadsl_compilationunit(javaDsl_CompilationUnit javadsl_compilationunit) {
        this.javadsl_compilationunit = javadsl_compilationunit;
    }

}