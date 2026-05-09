





import java.util.List;
import java.util.ArrayList;

public class qvtbase_Domain extends NamedElement {

    private String isCheckable;
    private String isEnforceable;



    public qvtbase_Domain(
        String isCheckable,        String isEnforceable    ) {
        super(
        );
        this.isCheckable = isCheckable;
        this.isEnforceable = isEnforceable;
    }


    public String getIscheckable() {
        return isCheckable;
    }

    public void setIscheckable(String isCheckable) {
        this.isCheckable = isCheckable;
    }
    public String getIsenforceable() {
        return isEnforceable;
    }

    public void setIsenforceable(String isEnforceable) {
        this.isEnforceable = isEnforceable;
    }


}