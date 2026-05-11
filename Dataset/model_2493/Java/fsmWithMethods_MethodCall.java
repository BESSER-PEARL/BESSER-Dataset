





import java.util.List;
import java.util.ArrayList;

public class fsmWithMethods_MethodCall extends FExpression {






    private List<fsmWithMethods_Referentiable> fsmwithmethods_referentiables;




    private fsmWithMethods_Method fsmwithmethods_method;


    public fsmWithMethods_MethodCall(
    ) {
        super(
        );
        this.fsmwithmethods_referentiables = new ArrayList<>();
    }

    public fsmWithMethods_MethodCall(
        ArrayList<fsmWithMethods_Referentiable> fsmwithmethods_referentiables    ) {
        this.fsmwithmethods_referentiables = fsmwithmethods_referentiables;
    }


    public List<fsmWithMethods_Referentiable> getFsmwithmethods_referentiables() {
        return fsmwithmethods_referentiables;
    }

    public void addFsmwithmethods_referentiable(Fsmwithmethods_referentiable fsmwithmethods_referentiable) {
        this.fsmwithmethods_referentiables.add(fsmwithmethods_referentiable);
    }
    public fsmWithMethods_Method getFsmwithmethods_method() {
        return fsmwithmethods_method;
    }

    public void setFsmwithmethods_method(fsmWithMethods_Method fsmwithmethods_method) {
        this.fsmwithmethods_method = fsmwithmethods_method;
    }

}