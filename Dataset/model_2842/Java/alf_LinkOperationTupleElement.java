





import java.util.List;
import java.util.ArrayList;

public class alf_LinkOperationTupleElement  {

    private String objectOrRole;





    private alf_Expression alf_expression;




    private alf_ValueSpecification alf_valuespecification;




    private alf_LinkOperationTuple alf_linkoperationtuple;


    public alf_LinkOperationTupleElement(
        String objectOrRole    ) {
        this.objectOrRole = objectOrRole;
    }


    public String getObjectorrole() {
        return objectOrRole;
    }

    public void setObjectorrole(String objectOrRole) {
        this.objectOrRole = objectOrRole;
    }

    public alf_Expression getAlf_expression() {
        return alf_expression;
    }

    public void setAlf_expression(alf_Expression alf_expression) {
        this.alf_expression = alf_expression;
    }
    public alf_ValueSpecification getAlf_valuespecification() {
        return alf_valuespecification;
    }

    public void setAlf_valuespecification(alf_ValueSpecification alf_valuespecification) {
        this.alf_valuespecification = alf_valuespecification;
    }
    public alf_LinkOperationTuple getAlf_linkoperationtuple() {
        return alf_linkoperationtuple;
    }

    public void setAlf_linkoperationtuple(alf_LinkOperationTuple alf_linkoperationtuple) {
        this.alf_linkoperationtuple = alf_linkoperationtuple;
    }

}