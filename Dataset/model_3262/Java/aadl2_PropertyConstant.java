





import java.util.List;
import java.util.ArrayList;

public class aadl2_PropertyConstant extends TypedElement, AbstractNamedValue, ArraySizeProperty {






    private aadl2_PropertySet aadl2_propertyset;




    private aadl2_PropertyExpression aadl2_propertyexpression;


    public aadl2_PropertyConstant(
    ) {
        super(
        );
    }



    public aadl2_PropertySet getAadl2_propertyset() {
        return aadl2_propertyset;
    }

    public void setAadl2_propertyset(aadl2_PropertySet aadl2_propertyset) {
        this.aadl2_propertyset = aadl2_propertyset;
    }
    public aadl2_PropertyExpression getAadl2_propertyexpression() {
        return aadl2_propertyexpression;
    }

    public void setAadl2_propertyexpression(aadl2_PropertyExpression aadl2_propertyexpression) {
        this.aadl2_propertyexpression = aadl2_propertyexpression;
    }

}