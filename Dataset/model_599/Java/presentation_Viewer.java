





import java.util.List;
import java.util.ArrayList;

public class presentation_Viewer  {

    private String group;
    private String mixed;



    public presentation_Viewer(
        String group,        String mixed    ) {
        this.group = group;
        this.mixed = mixed;
    }


    public String getGroup() {
        return group;
    }

    public void setGroup(String group) {
        this.group = group;
    }
    public String getMixed() {
        return mixed;
    }

    public void setMixed(String mixed) {
        this.mixed = mixed;
    }


}