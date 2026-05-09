





import java.util.List;
import java.util.ArrayList;

public class fIDL_VectorType extends Type {

    private boolean nullable;





    private fIDL_Constant fidl_constant;




    private fIDL_Type fidl_type;


    public fIDL_VectorType(
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
    public fIDL_Type getFidl_type() {
        return fidl_type;
    }

    public void setFidl_type(fIDL_Type fidl_type) {
        this.fidl_type = fidl_type;
    }

}