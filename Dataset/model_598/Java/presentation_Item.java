





import java.util.List;
import java.util.ArrayList;

public class presentation_Item extends Widget {

    private String image;
    private String text;



    public presentation_Item(
        String image,        String text    ) {
        super(
        );
        this.image = image;
        this.text = text;
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