





import java.util.List;
import java.util.ArrayList;

public class gast_accesses_DelegateAccess extends FunctionAccess {






    private Delegate delegate;




    private List<Function> functions;


    public gast_accesses_DelegateAccess(
    ) {
        super(
        );
        this.functions = new ArrayList<>();
    }

    public gast_accesses_DelegateAccess(
        ArrayList<Function> functions    ) {
        this.functions = functions;
    }


    public Delegate getDelegate() {
        return delegate;
    }

    public void setDelegate(Delegate delegate) {
        this.delegate = delegate;
    }
    public List<Function> getFunctions() {
        return functions;
    }

    public void addFunction(Function function) {
        this.functions.add(function);
    }

}