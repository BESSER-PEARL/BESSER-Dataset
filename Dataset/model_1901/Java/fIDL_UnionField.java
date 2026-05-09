





import java.util.List;
import java.util.ArrayList;

public class fIDL_UnionField extends UnionMember {

    private String name;





    private fIDL_Type fidl_type;


    public fIDL_UnionField(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public fIDL_Type getFidl_type() {
        return fidl_type;
    }

    public void setFidl_type(fIDL_Type fidl_type) {
        this.fidl_type = fidl_type;
    }

}