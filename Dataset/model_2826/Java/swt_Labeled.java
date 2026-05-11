





import java.util.List;
import java.util.ArrayList;

public class swt_Labeled  {

    private String text;
    private String image;



    public swt_Labeled(
        String text,        String image    ) {
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