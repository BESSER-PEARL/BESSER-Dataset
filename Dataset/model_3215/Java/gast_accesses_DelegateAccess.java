





import java.util.List;
import java.util.ArrayList;

public class gast_accesses_DelegateAccess extends FunctionAccess {






    private List<Function> functions;




    private Delegate delegate;


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


    public List<Function> getFunctions() {
        return functions;
    }

    public void addFunction(Function function) {
        this.functions.add(function);
    }
    public Delegate getDelegate() {
        return delegate;
    }

    public void setDelegate(Delegate delegate) {
        this.delegate = delegate;
    }

}