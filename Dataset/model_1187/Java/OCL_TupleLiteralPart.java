





import java.util.List;
import java.util.ArrayList;

public class OCL_TupleLiteralPart extends TypedElement {






    private Property property;




    private OclExpression oclexpression;


    public OCL_TupleLiteralPart(
    ) {
        super(
        );
    }



    public Property getProperty() {
        return property;
    }

    public void setProperty(Property property) {
        this.property = property;
    }
    public OclExpression getOclexpression() {
        return oclexpression;
    }

    public void setOclexpression(OclExpression oclexpression) {
        this.oclexpression = oclexpression;
    }

}