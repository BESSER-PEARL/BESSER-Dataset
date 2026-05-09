





import java.util.List;
import java.util.ArrayList;

public class uma_TextElement extends LeafElement {

    private String text;



    public uma_TextElement(
        String text    ) {
        super(
        );
        this.text = text;
    }


    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }


}