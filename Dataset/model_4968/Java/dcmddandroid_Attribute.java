





import java.util.List;
import java.util.ArrayList;

public class dcmddandroid_Attribute extends ClassElement {

    private String type;
    private String secured;
    private String defaultValue;





    private dcmddandroid_AbstractClass dcmddandroid_abstractclass;


    public dcmddandroid_Attribute(
        String type,        String secured,        String defaultValue    ) {
        super(
        );
        this.type = type;
        this.secured = secured;
        this.defaultValue = defaultValue;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getSecured() {
        return secured;
    }

    public void setSecured(String secured) {
        this.secured = secured;
    }
    public String getDefaultvalue() {
        return defaultValue;
    }

    public void setDefaultvalue(String defaultValue) {
        this.defaultValue = defaultValue;
    }

    public dcmddandroid_AbstractClass getDcmddandroid_abstractclass() {
        return dcmddandroid_abstractclass;
    }

    public void setDcmddandroid_abstractclass(dcmddandroid_AbstractClass dcmddandroid_abstractclass) {
        this.dcmddandroid_abstractclass = dcmddandroid_abstractclass;
    }

}