





import java.util.List;
import java.util.ArrayList;

public class types_Property extends Declaration {

    private boolean const;
    private boolean external;
    private boolean readonly;





    private types_Annotation types_annotation;


    public types_Property(
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

    public types_Annotation getTypes_annotation() {
        return types_annotation;
    }

    public void setTypes_annotation(types_Annotation types_annotation) {
        this.types_annotation = types_annotation;
    }

}