





import java.util.List;
import java.util.ArrayList;

public class java__ImportDeclaration extends ASTNode {

    private boolean static;



    public java__ImportDeclaration(
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