





import java.util.List;
import java.util.ArrayList;

public class fIDL_StringType extends Type {

    private boolean nullable;





    private fIDL_Constant fidl_constant;


    public fIDL_StringType(
        boolean nullable    ) {
        super(
        );
        this.nullable = nullable;
    }


    public boolean getNullable() {
        return nullable;
    }

    public void setNullable(boolean nullable) {
        this.nullable = nullable;
    }

    public fIDL_Constant getFidl_constant() {
        return fidl_constant;
    }

    public void setFidl_constant(fIDL_Constant fidl_constant) {
        this.fidl_constant = fidl_constant;
    }

}