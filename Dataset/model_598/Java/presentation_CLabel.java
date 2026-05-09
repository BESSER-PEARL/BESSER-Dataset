





import java.util.List;
import java.util.ArrayList;

public class presentation_CLabel extends Canvas {

    private String image;
    private String text;
    private String alignment;



    public presentation_CLabel(
        String image,        String text,        String alignment    ) {
        super(
        );
        this.image = image;
        this.text = text;
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
    public String getAlignment() {
        return alignment;
    }

    public void setAlignment(String alignment) {
        this.alignment = alignment;
    }


}