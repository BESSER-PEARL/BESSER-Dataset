





import java.util.List;
import java.util.ArrayList;

public class presentation_CLabel extends Canvas {

    private String alignment;
    private String text;
    private String image;



    public presentation_CLabel(
        String alignment,        String text,        String image    ) {
        super(
        );
        this.alignment = alignment;
        this.text = text;
        this.image = image;
    }


    public String getAlignment() {
        return alignment;
    }

    public void setAlignment(String alignment) {
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


}