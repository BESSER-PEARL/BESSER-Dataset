





import java.util.List;
import java.util.ArrayList;

public class presentation_Label extends Control {

    private String text;
    private String image;
    private String alignment;



    public presentation_Label(
        String text,        String image,        String alignment    ) {
        super(
        );
        this.text = text;
        this.image = image;
        this.alignment = alignment;
    }


    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }
    public String getImage() {
        return image;
    }

    public void setImage(String image) {
        this.image = image;
    }
    public String getAlignment() {
        return alignment;
    }

    public void setAlignment(String alignment) {
        this.alignment = alignment;
    }


}