





import java.util.List;
import java.util.ArrayList;

public class QVTCore_PropertyAssignment extends Assignment {






    private Property property;




    private OclExpression oclexpression;


    public QVTCore_PropertyAssignment(
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