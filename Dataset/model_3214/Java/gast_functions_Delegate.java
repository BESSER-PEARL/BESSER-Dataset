





import java.util.List;
import java.util.ArrayList;

public class gast_functions_Delegate extends functions_Function, types_GASTType, types_Member {

    private boolean innerDelegate;





    private GASTClass gastclass;




    private GASTClass gastclass;




    private Package package;




    private List<Function> functions;


    public gast_functions_Delegate(
        boolean innerDelegate    ) {
        super(
        );
        this.innerDelegate = innerDelegate;
        this.functions = new ArrayList<>();
    }

    public gast_functions_Delegate(
        boolean innerDelegate        ArrayList<Function> functions    ) {
        this.innerDelegate = innerDelegate;
        this.functions = functions;
    }

    public boolean getInnerdelegate() {
        return innerDelegate;
    }

    public void setInnerdelegate(boolean innerDelegate) {
        this.innerDelegate = innerDelegate;
    }

    public GASTClass getGastclass() {
        return gastclass;
    }

    public void setGastclass(GASTClass gastclass) {
        this.gastclass = gastclass;
    }
    public GASTClass getGastclass() {
        return gastclass;
    }

    public void setGastclass(GASTClass gastclass) {
        this.gastclass = gastclass;
    }
    public Package getPackage() {
        return package;
    }

    public void setPackage(Package package) {
        this.package = package;
    }
    public List<Function> getFunctions() {
        return functions;
    }

    public void addFunction(Function function) {
        this.functions.add(function);
    }

}