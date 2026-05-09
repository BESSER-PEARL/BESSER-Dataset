





import java.util.List;
import java.util.ArrayList;

public class DOM_ImportDeclaration extends ASTNode {

    private String static;
    private String onDemand;



    public DOM_ImportDeclaration(
        String static,        String onDemand    ) {
        super(
        );
        this.static = static;
        this.onDemand = onDemand;
    }


    public String getStatic() {
        return static;
    }

    public void setStatic(String static) {
        this.static = static;
    }
    public String getOndemand() {
        return onDemand;
    }

    public void setOndemand(String onDemand) {
        this.onDemand = onDemand;
    }


}