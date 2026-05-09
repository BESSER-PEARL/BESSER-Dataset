





import java.util.List;
import java.util.ArrayList;

public class fIDL_ArrayType extends Type {






    private fIDL_Type fidl_type;




    private fIDL_Constant fidl_constant;


    public fIDL_ArrayType(
    ) {
        super(
        );
    }



    public fIDL_Type getFidl_type() {
        return fidl_type;
    }

    public void setFidl_type(fIDL_Type fidl_type) {
        this.fidl_type = fidl_type;
    }
    public fIDL_Constant getFidl_constant() {
        return fidl_constant;
    }

    public void setFidl_constant(fIDL_Constant fidl_constant) {
        this.fidl_constant = fidl_constant;
    }

}