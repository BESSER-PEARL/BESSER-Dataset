





import java.util.List;
import java.util.ArrayList;

public class model_xbase_XObjectLiteralPart  {

    private String name;





    private XExpression xexpression;


    public model_xbase_XObjectLiteralPart(
        String name    ) {
        this.name = name;
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