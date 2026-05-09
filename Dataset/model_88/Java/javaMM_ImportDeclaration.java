





import java.util.List;
import java.util.ArrayList;

public class javaMM_ImportDeclaration extends ASTNode {

    private boolean static;



    public javaMM_ImportDeclaration(
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