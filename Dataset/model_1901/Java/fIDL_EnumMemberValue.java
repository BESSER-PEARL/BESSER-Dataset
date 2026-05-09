





import java.util.List;
import java.util.ArrayList;

public class fIDL_EnumMemberValue  {

    private String value;





    private fIDL_EnumMember fidl_enummember;


    public fIDL_EnumMemberValue(
        String value    ) {
        this.value = value;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public fIDL_EnumMember getFidl_enummember() {
        return fidl_enummember;
    }

    public void setFidl_enummember(fIDL_EnumMember fidl_enummember) {
        this.fidl_enummember = fidl_enummember;
    }

}