





import java.util.List;
import java.util.ArrayList;

public class fIDL_ConstDeclaration extends Declaration, InterfaceMember {






    private fIDL_StructMember fidl_structmember;


    public fIDL_ConstDeclaration(
    ) {
        super(
        );
    }



    public fIDL_StructMember getFidl_structmember() {
        return fidl_structmember;
    }

    public void setFidl_structmember(fIDL_StructMember fidl_structmember) {
        this.fidl_structmember = fidl_structmember;
    }

}