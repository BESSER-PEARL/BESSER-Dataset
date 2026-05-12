





import java.util.List;
import java.util.ArrayList;

public class sqlmodel_datatypes_AttributeDefinition extends TypedElement {

    private String defaultValue;
    private boolean scopeChecked;
    private String scopeCheck;



    public sqlmodel_datatypes_AttributeDefinition(
        String defaultValue,        boolean scopeChecked,        String scopeCheck    ) {
        super(
        );
        this.defaultValue = defaultValue;
        this.scopeChecked = scopeChecked;
        this.scopeCheck = scopeCheck;
    }


    public String getDefaultvalue() {
        return defaultValue;
    }

    public void setDefaultvalue(String defaultValue) {
        this.defaultValue = defaultValue;
    }
    public boolean getScopechecked() {
        return scopeChecked;
    }

    public void setScopechecked(boolean scopeChecked) {
        this.scopeChecked = scopeChecked;
    }
    public String getScopecheck() {
        return scopeCheck;
    }

    public void setScopecheck(String scopeCheck) {
        this.scopeCheck = scopeCheck;
    }


}