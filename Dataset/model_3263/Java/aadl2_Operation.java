





import java.util.List;
import java.util.ArrayList;

public class aadl2_Operation extends PropertyExpression {

    private String op;





    private List<aadl2_PropertyExpression> aadl2_propertyexpressions;


    public aadl2_Operation(
        String op    ) {
        super(
        );
        this.op = op;
        this.aadl2_propertyexpressions = new ArrayList<>();
    }

    public aadl2_Operation(
        String op        ArrayList<aadl2_PropertyExpression> aadl2_propertyexpressions    ) {
        this.op = op;
        this.aadl2_propertyexpressions = aadl2_propertyexpressions;
    }

    public String getOp() {
        return op;
    }

    public void setOp(String op) {
        this.op = op;
    }

    public List<aadl2_PropertyExpression> getAadl2_propertyexpressions() {
        return aadl2_propertyexpressions;
    }

    public void addAadl2_propertyexpression(Aadl2_propertyexpression aadl2_propertyexpression) {
        this.aadl2_propertyexpressions.add(aadl2_propertyexpression);
    }

}