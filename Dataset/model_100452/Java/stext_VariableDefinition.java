





import java.util.List;
import java.util.ArrayList;

public class stext_VariableDefinition extends Variable {

    private boolean readonly;
    private boolean external;
    private String type;
    private String initialValue;



    public stext_VariableDefinition(
        boolean readonly,        boolean external,        String type,        String initialValue    ) {
        super(
        );
        this.readonly = readonly;
        this.external = external;
        this.type = type;
        this.initialValue = initialValue;
    }


    public boolean getReadonly() {
        return readonly;
    }

    public void setReadonly(boolean readonly) {
        this.readonly = readonly;
    }
    public boolean getExternal() {
        return external;
    }

    public void setExternal(boolean external) {
        this.external = external;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getInitialvalue() {
        return initialValue;
    }

    public void setInitialvalue(String initialValue) {
        this.initialValue = initialValue;
    }


}