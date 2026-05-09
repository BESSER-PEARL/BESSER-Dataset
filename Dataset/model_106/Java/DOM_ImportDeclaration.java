





import java.util.List;
import java.util.ArrayList;

public class DOM_ImportDeclaration extends ASTNode {

    private String onDemand;
    private String static;



    public DOM_ImportDeclaration(
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


}