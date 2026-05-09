





import java.util.List;
import java.util.ArrayList;

public class QVTCore_PropertyAssignment extends Assignment {






    private OclExpression oclexpression;




    private Property property;


    public QVTCore_PropertyAssignment(
    ) {
        super(
        );
    }



    public OclExpression getOclexpression() {
        return oclexpression;
    }

    public void setOclexpression(OclExpression oclexpression) {
        this.oclexpression = oclexpression;
    }
    public Property getProperty() {
        return property;
    }

    public void setProperty(Property property) {
        this.property = property;
    }

}