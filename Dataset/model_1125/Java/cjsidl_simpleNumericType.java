





import java.util.List;
import java.util.ArrayList;

public class cjsidl_simpleNumericType  {

    private String type;





    private cjsidl_constDef cjsidl_constdef;


    public cjsidl_simpleNumericType(
        String type    ) {
        this.type = type;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public cjsidl_constDef getCjsidl_constdef() {
        return cjsidl_constdef;
    }

    public void setCjsidl_constdef(cjsidl_constDef cjsidl_constdef) {
        this.cjsidl_constdef = cjsidl_constdef;
    }

}