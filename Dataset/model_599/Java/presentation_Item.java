





import java.util.List;
import java.util.ArrayList;

public class presentation_Item extends Widget {

    private String text;
    private String image;



    public presentation_Item(
        String text,        String image    ) {
        super(
        );
        this.text = text;
        this.image = image;
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