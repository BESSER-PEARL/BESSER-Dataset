





import java.util.List;
import java.util.ArrayList;

public class fIDL_StructField  {

    private String name;





    private fIDL_Constant fidl_constant;




    private fIDL_StructMember fidl_structmember;




    private fIDL_Type fidl_type;


    public fIDL_StructField(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public fIDL_Constant getFidl_constant() {
        return fidl_constant;
    }

    public void setFidl_constant(fIDL_Constant fidl_constant) {
        this.fidl_constant = fidl_constant;
    }
    public fIDL_StructMember getFidl_structmember() {
        return fidl_structmember;
    }

    public void setFidl_structmember(fIDL_StructMember fidl_structmember) {
        this.fidl_structmember = fidl_structmember;
    }
    public fIDL_Type getFidl_type() {
        return fidl_type;
    }

    public void setFidl_type(fIDL_Type fidl_type) {
        this.fidl_type = fidl_type;
    }

}