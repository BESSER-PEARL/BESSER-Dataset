





import java.util.List;
import java.util.ArrayList;

public class simpleocl_PropertyCallExp extends OclExpression {






    private List<simpleocl_PropertyCall> simpleocl_propertycalls;




    private simpleocl_OclExpression simpleocl_oclexpression;




    private simpleocl_OclExpression simpleocl_oclexpression;




    private simpleocl_PropertyCall simpleocl_propertycall;


    public simpleocl_PropertyCallExp(
    ) {
        super(
        );
        this.simpleocl_propertycalls = new ArrayList<>();
    }

    public simpleocl_PropertyCallExp(
        ArrayList<simpleocl_PropertyCall> simpleocl_propertycalls    ) {
        this.simpleocl_propertycalls = simpleocl_propertycalls;
    }


    public List<simpleocl_PropertyCall> getSimpleocl_propertycalls() {
        return simpleocl_propertycalls;
    }

    public void addSimpleocl_propertycall(Simpleocl_propertycall simpleocl_propertycall) {
        this.simpleocl_propertycalls.add(simpleocl_propertycall);
    }
    public simpleocl_OclExpression getSimpleocl_oclexpression() {
        return simpleocl_oclexpression;
    }

    public void setSimpleocl_oclexpression(simpleocl_OclExpression simpleocl_oclexpression) {
        this.simpleocl_oclexpression = simpleocl_oclexpression;
    }
    public simpleocl_OclExpression getSimpleocl_oclexpression() {
        return simpleocl_oclexpression;
    }

    public void setSimpleocl_oclexpression(simpleocl_OclExpression simpleocl_oclexpression) {
        this.simpleocl_oclexpression = simpleocl_oclexpression;
    }
    public simpleocl_PropertyCall getSimpleocl_propertycall() {
        return simpleocl_propertycall;
    }

    public void setSimpleocl_propertycall(simpleocl_PropertyCall simpleocl_propertycall) {
        this.simpleocl_propertycall = simpleocl_propertycall;
    }

}