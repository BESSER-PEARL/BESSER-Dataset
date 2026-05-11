





import java.util.List;
import java.util.ArrayList;

public class gast_functions_Delegate extends types_GASTType, functions_Function, types_Member {

    private boolean innerDelegate;





    private Package package;


    public gast_functions_Delegate(
        boolean innerDelegate    ) {
        super(
        );
        this.innerDelegate = innerDelegate;
    }


    public boolean getInnerdelegate() {
        return innerDelegate;
    }

    public void setInnerdelegate(boolean innerDelegate) {
        this.innerDelegate = innerDelegate;
    }

    public Package getPackage() {
        return package;
    }

    public void setPackage(Package package) {
        this.package = package;
    }

}