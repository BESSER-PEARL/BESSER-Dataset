





import java.util.List;
import java.util.ArrayList;

public class presentation_AbstractDataProvider  {

    private String mixed;
    private String group;
    private String key;



    public presentation_AbstractDataProvider(
        String mixed,        String group,        String key    ) {
        this.mixed = mixed;
        this.group = group;
        this.key = key;
    }


    public String getMixed() {
        return mixed;
    }

    public void setMixed(String mixed) {
        this.mixed = mixed;
    }
    public String getGroup() {
        return group;
    }

    public void setGroup(String group) {
        this.group = group;
    }
    public String getKey() {
        return key;
    }

    public void setKey(String key) {
        this.key = key;
    }


}