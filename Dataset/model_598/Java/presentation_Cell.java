





import java.util.List;
import java.util.ArrayList;

public class presentation_Cell  {

    private String text;
    private String group;
    private String mixed;
    private String image;



    public presentation_Cell(
        String text,        String group,        String mixed,        String image    ) {
        this.text = text;
        this.group = group;
        this.mixed = mixed;
        this.image = image;
    }


    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
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
    public String getImage() {
        return image;
    }

    public void setImage(String image) {
        this.image = image;
    }


}