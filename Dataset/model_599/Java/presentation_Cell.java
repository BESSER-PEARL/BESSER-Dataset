





import java.util.List;
import java.util.ArrayList;

public class presentation_Cell  {

    private String image;
    private String mixed;
    private String text;
    private String group;



    public presentation_Cell(
        String image,        String mixed,        String text,        String group    ) {
        this.image = image;
        this.mixed = mixed;
        this.text = text;
        this.group = group;
    }


    public String getImage() {
        return image;
    }

    public void setImage(String image) {
        this.image = image;
    }
    public String getMixed() {
        return mixed;
    }

    public void setMixed(String mixed) {
        this.mixed = mixed;
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


}