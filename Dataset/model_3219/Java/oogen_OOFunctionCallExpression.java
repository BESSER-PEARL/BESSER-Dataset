





import java.util.List;
import java.util.ArrayList;

public class oogen_OOFunctionCallExpression extends OOExpression {

    private String functionName;





    private List<oogen_OOExpression> oogen_ooexpressions;




    private oogen_OOExpression oogen_ooexpression;


    public oogen_OOFunctionCallExpression(
        String functionName    ) {
        super(
        );
        this.functionName = functionName;
        this.oogen_ooexpressions = new ArrayList<>();
    }

    public oogen_OOFunctionCallExpression(
        String functionName        ArrayList<oogen_OOExpression> oogen_ooexpressions    ) {
        this.functionName = functionName;
        this.oogen_ooexpressions = oogen_ooexpressions;
    }

    public String getFunctionname() {
        return functionName;
    }

    public void setFunctionname(String functionName) {
        this.functionName = functionName;
    }

    public List<oogen_OOExpression> getOogen_ooexpressions() {
        return oogen_ooexpressions;
    }

    public void addOogen_ooexpression(Oogen_ooexpression oogen_ooexpression) {
        this.oogen_ooexpressions.add(oogen_ooexpression);
    }
    public oogen_OOExpression getOogen_ooexpression() {
        return oogen_ooexpression;
    }

    public void setOogen_ooexpression(oogen_OOExpression oogen_ooexpression) {
        this.oogen_ooexpression = oogen_ooexpression;
    }

}