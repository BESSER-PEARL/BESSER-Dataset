





import java.util.List;
import java.util.ArrayList;

public class stext_VariableDefinition extends Variable, Property {

    private boolean const;
    private boolean external;
    private boolean readonly;



    public stext_VariableDefinition(
        boolean const,        boolean external,        boolean readonly    ) {
        super(
        );
        this.const = const;
        this.external = external;
        this.readonly = readonly;
    }


    public boolean getConst() {
        return const;
    }

    public void setConst(boolean const) {
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


}