





import java.util.List;
import java.util.ArrayList;

public class fIDL_EnumMember  {

    private String name;





    private fIDL_EnumDeclaration fidl_enumdeclaration;


    public fIDL_EnumMember(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public fIDL_EnumDeclaration getFidl_enumdeclaration() {
        return fidl_enumdeclaration;
    }

    public void setFidl_enumdeclaration(fIDL_EnumDeclaration fidl_enumdeclaration) {
        this.fidl_enumdeclaration = fidl_enumdeclaration;
    }

}