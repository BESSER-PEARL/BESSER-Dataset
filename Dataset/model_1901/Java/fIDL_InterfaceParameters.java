





import java.util.List;
import java.util.ArrayList;

public class fIDL_InterfaceParameters  {

    private String name;
    private String resultName;





    private fIDL_InterfaceMethod fidl_interfacemethod;


    public fIDL_InterfaceParameters(
        String name,        String resultName    ) {
        this.name = name;
        this.resultName = resultName;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getResultname() {
        return resultName;
    }

    public void setResultname(String resultName) {
        this.resultName = resultName;
    }

    public fIDL_InterfaceMethod getFidl_interfacemethod() {
        return fidl_interfacemethod;
    }

    public void setFidl_interfacemethod(fIDL_InterfaceMethod fidl_interfacemethod) {
        this.fidl_interfacemethod = fidl_interfacemethod;
    }

}