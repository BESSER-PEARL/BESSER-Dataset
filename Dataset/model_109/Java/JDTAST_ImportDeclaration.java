





import java.util.List;
import java.util.ArrayList;

public class JDTAST_ImportDeclaration extends ASTNode {

    private String onDemand;
    private String static;





    private JDTAST_CompilationUnit jdtast_compilationunit;


    public JDTAST_ImportDeclaration(
        String onDemand,        String static    ) {
        super(
        );
        this.onDemand = onDemand;
        this.static = static;
    }


    public String getOndemand() {
        return onDemand;
    }

    public void setOndemand(String onDemand) {
        this.onDemand = onDemand;
    }
    public String getStatic() {
        return static;
    }

    public void setStatic(String static) {
        this.static = static;
    }

    public JDTAST_CompilationUnit getJdtast_compilationunit() {
        return jdtast_compilationunit;
    }

    public void setJdtast_compilationunit(JDTAST_CompilationUnit jdtast_compilationunit) {
        this.jdtast_compilationunit = jdtast_compilationunit;
    }

}