





import java.util.List;
import java.util.ArrayList;

public class aadl2_ListValue extends PropertyExpression {






    private List<aadl2_PropertyExpression> aadl2_propertyexpressions;


    public aadl2_ListValue(
    ) {
        super(
        );
        this.aadl2_propertyexpressions = new ArrayList<>();
    }

    public aadl2_ListValue(
        ArrayList<aadl2_PropertyExpression> aadl2_propertyexpressions    ) {
        this.aadl2_propertyexpressions = aadl2_propertyexpressions;
    }


    public List<aadl2_PropertyExpression> getAadl2_propertyexpressions() {
        return aadl2_propertyexpressions;
    }

    public void addAadl2_propertyexpression(Aadl2_propertyexpression aadl2_propertyexpression) {
        this.aadl2_propertyexpressions.add(aadl2_propertyexpression);
    }

}