





import java.util.List;
import java.util.ArrayList;

public class javaMM_ImportDeclaration extends ASTNode {

    private String static;



    public javaMM_ImportDeclaration(
        String static    ) {
        super(
        );
        this.static = static;
    }


    public String getStatic() {
        return static;
    }

    public void setStatic(String static) {
        this.static = static;
    }


}