





import java.util.List;
import java.util.ArrayList;

public class java_ImportDeclaration extends ASTNode {

    private boolean static;



    public java_ImportDeclaration(
        boolean static    ) {
        super(
        );
        this.static = static;
    }


    public boolean getStatic() {
        return static;
    }

    public void setStatic(boolean static) {
        this.static = static;
    }


}