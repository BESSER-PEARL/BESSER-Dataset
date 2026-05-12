





import java.util.List;
import java.util.ArrayList;

public class sqlmodel_tables_Column extends TypedElement {

    private String defaultValue;
    private boolean nullable;
    private String scopeCheck;
    private boolean implementationDependent;
    private boolean scopeChecked;





    private Table table;


    public sqlmodel_tables_Column(
        String defaultValue,        boolean nullable,        String scopeCheck,        boolean implementationDependent,        boolean scopeChecked    ) {
        super(
        );
        this.defaultValue = defaultValue;
        this.nullable = nullable;
        this.scopeCheck = scopeCheck;
        this.implementationDependent = implementationDependent;
        this.scopeChecked = scopeChecked;
    }


    public String getDefaultvalue() {
        return defaultValue;
    }

    public void setDefaultvalue(String defaultValue) {
        this.defaultValue = defaultValue;
    }
    public boolean getNullable() {
        return nullable;
    }

    public void setNullable(boolean nullable) {
        this.nullable = nullable;
    }
    public String getScopecheck() {
        return scopeCheck;
    }

    public void setScopecheck(String scopeCheck) {
        this.scopeCheck = scopeCheck;
    }
    public boolean getImplementationdependent() {
        return implementationDependent;
    }

    public void setImplementationdependent(boolean implementationDependent) {
        this.implementationDependent = implementationDependent;
    }
    public boolean getScopechecked() {
        return scopeChecked;
    }

    public void setScopechecked(boolean scopeChecked) {
        this.scopeChecked = scopeChecked;
    }

    public Table getTable() {
        return table;
    }

    public void setTable(Table table) {
        this.table = table;
    }

}