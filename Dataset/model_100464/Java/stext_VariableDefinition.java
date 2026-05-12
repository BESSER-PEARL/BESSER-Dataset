





import java.util.List;
import java.util.ArrayList;

public class stext_VariableDefinition extends Variable {

    private boolean external;
    private String initialValue;
    private String type;
    private boolean readonly;



    public stext_VariableDefinition(
        boolean external,        String initialValue,        String type,        boolean readonly    ) {
        super(
        );
        this.external = external;
        this.initialValue = initialValue;
        this.type = type;
        this.readonly = readonly;
    }


    public boolean getExternal() {
        return external;
    }

    public void setExternal(boolean external) {
        this.external = external;
    }
    public String getInitialvalue() {
        return initialValue;
    }

    public void setInitialvalue(String initialValue) {
        this.initialValue = initialValue;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public boolean getReadonly() {
        return readonly;
    }

    public void setReadonly(boolean readonly) {
        this.readonly = readonly;
    }


}