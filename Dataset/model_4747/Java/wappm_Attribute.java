





import java.util.List;
import java.util.ArrayList;

public class wappm_Attribute  {

    private String name;
    private String type;





    private wappm_WebClass wappm_webclass;


    public wappm_Attribute(
        String name,        String type    ) {
        this.name = name;
        this.type = type;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public wappm_WebClass getWappm_webclass() {
        return wappm_webclass;
    }

    public void setWappm_webclass(wappm_WebClass wappm_webclass) {
        this.wappm_webclass = wappm_webclass;
    }

}