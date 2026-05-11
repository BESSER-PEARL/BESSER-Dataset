





import java.util.List;
import java.util.ArrayList;

public class model_types_JvmFormalParameter extends JvmAnnotationTarget {

    private boolean varArg;
    private String name;





    private XExpression xexpression;


    public model_types_JvmFormalParameter(
        boolean varArg,        String name    ) {
        super(
        );
        this.varArg = varArg;
        this.name = name;
    }


    public boolean getVararg() {
        return varArg;
    }

    public void setVararg(boolean varArg) {
        this.varArg = varArg;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public XExpression getXexpression() {
        return xexpression;
    }

    public void setXexpression(XExpression xexpression) {
        this.xexpression = xexpression;
    }

}