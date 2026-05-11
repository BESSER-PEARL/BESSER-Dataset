





import java.util.List;
import java.util.ArrayList;

public class types_Property extends TypedDeclaration {

    private boolean readonly;
    private boolean const;



    public types_Property(
        boolean readonly,        boolean const    ) {
        super(
        );
        this.readonly = readonly;
        this.const = const;
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