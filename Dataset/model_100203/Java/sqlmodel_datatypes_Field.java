





import java.util.List;
import java.util.ArrayList;

public class sqlmodel_datatypes_Field extends TypedElement {

    private String scopeCheck;
    private boolean scopeChecked;



    public sqlmodel_datatypes_Field(
        String scopeCheck,        boolean scopeChecked    ) {
        super(
        );
        this.scopeCheck = scopeCheck;
        this.scopeChecked = scopeChecked;
    }


    public String getScopecheck() {
        return scopeCheck;
    }

    public void setScopecheck(String scopeCheck) {
        this.scopeCheck = scopeCheck;
    }
    public boolean getScopechecked() {
        return scopeChecked;
    }

    public void setScopechecked(boolean scopeChecked) {
        this.scopeChecked = scopeChecked;
    }


}