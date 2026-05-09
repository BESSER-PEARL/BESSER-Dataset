





import java.util.List;
import java.util.ArrayList;

public class fIDL_Parameter  {

    private String name;





    private fIDL_ParameterList fidl_parameterlist;


    public fIDL_Parameter(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public fIDL_ParameterList getFidl_parameterlist() {
        return fidl_parameterlist;
    }

    public void setFidl_parameterlist(fIDL_ParameterList fidl_parameterlist) {
        this.fidl_parameterlist = fidl_parameterlist;
    }

}