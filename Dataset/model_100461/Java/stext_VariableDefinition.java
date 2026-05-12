





import java.util.List;
import java.util.ArrayList;

public class stext_VariableDefinition extends Variable, Property {

    private boolean external;
    private boolean readonly;
    private boolean const;



    public stext_VariableDefinition(
        boolean external,        boolean readonly,        boolean const    ) {
        super(
        );
        this.external = external;
        this.readonly = readonly;
        this.const = const;
    }


    public boolean getExternal() {
        return external;
    }

    public void setExternal(boolean external) {
        this.external = external;
    }
    public boolean getReadonly() {
        return readonly;
    }

    public void setReadonly(boolean readonly) {
        this.readonly = readonly;
    }
    public boolean getConst() {
        return const;
    }

    public void setConst(boolean const) {
        this.const = const;
    }


}