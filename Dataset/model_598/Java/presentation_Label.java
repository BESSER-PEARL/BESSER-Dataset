





import java.util.List;
import java.util.ArrayList;

public class presentation_Label extends Control {

    private String alignment;
    private String image;
    private String text;



    public presentation_Label(
        String alignment,        String image,        String text    ) {
        super(
        );
        this.alignment = alignment;
        this.image = image;
        this.text = text;
    }


    public String getAlignment() {
        return alignment;
    }

    public void setAlignment(String alignment) {
        this.alignment = alignment;
    }
    public String getImage() {
        return image;
    }

    public void setImage(String image) {
        this.image = image;
    }
    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }


}