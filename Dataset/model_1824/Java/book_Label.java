





import java.util.List;
import java.util.ArrayList;

public class book_Label extends Control {

    private String font;
    private String text;



    public book_Label(
        String font,        String text    ) {
        super(
        );
        this.font = font;
        this.text = text;
    }


    public String getFont() {
        return font;
    }

    public void setFont(String font) {
        this.font = font;
    }
    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }


}