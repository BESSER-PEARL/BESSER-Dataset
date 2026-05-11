





import java.util.List;
import java.util.ArrayList;

public class types_Property extends Declaration {

    private boolean readonly;
    private boolean const;
    private boolean external;



    public types_Property(
        boolean readonly,        boolean const,        boolean external    ) {
        super(
        );
        this.readonly = readonly;
        this.const = const;
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
    public boolean getExternal() {
        return external;
    }

    public void setExternal(boolean external) {
        this.external = external;
    }


}