





import java.util.List;
import java.util.ArrayList;

public class QVTBase_Domain extends NamedElement {

    private String isEnforceable;
    private String isCheckable;



    public QVTBase_Domain(
        String isEnforceable,        String isCheckable    ) {
        super(
        );
        this.isEnforceable = isEnforceable;
        this.isCheckable = isCheckable;
    }


    public String getIsenforceable() {
        return isEnforceable;
    }

    public void setIsenforceable(String isEnforceable) {
        this.isEnforceable = isEnforceable;
    }
    public String getIscheckable() {
        return isCheckable;
    }

    public void setIscheckable(String isCheckable) {
        this.isCheckable = isCheckable;
    }


}