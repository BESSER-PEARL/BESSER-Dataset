





import java.util.List;
import java.util.ArrayList;

public class gv_Attribute extends Commentable {

    private String value;
    private String key;





    private gv_AList gv_alist;


    public gv_Attribute(
        String value,        String key    ) {
        super(
        );
        this.value = value;
        this.key = key;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public String getKey() {
        return key;
    }

    public void setKey(String key) {
        this.key = key;
    }

    public gv_AList getGv_alist() {
        return gv_alist;
    }

    public void setGv_alist(gv_AList gv_alist) {
        this.gv_alist = gv_alist;
    }

}