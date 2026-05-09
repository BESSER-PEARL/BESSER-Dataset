





import java.util.List;
import java.util.ArrayList;

public class presentation_FormData  {

    private String mixed;
    private String height;
    private String group;
    private String width;



    public presentation_FormData(
        String mixed,        String height,        String group,        String width    ) {
        this.mixed = mixed;
        this.height = height;
        this.group = group;
        this.width = width;
    }


    public String getMixed() {
        return mixed;
    }

    public void setMixed(String mixed) {
        this.mixed = mixed;
    }
    public String getHeight() {
        return height;
    }

    public void setHeight(String height) {
        this.height = height;
    }
    public String getGroup() {
        return group;
    }

    public void setGroup(String group) {
        this.group = group;
    }
    public String getWidth() {
        return width;
    }

    public void setWidth(String width) {
        this.width = width;
    }


}