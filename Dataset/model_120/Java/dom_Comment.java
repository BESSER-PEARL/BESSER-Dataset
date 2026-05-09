





import java.util.List;
import java.util.ArrayList;

public class dom_Comment extends Node {

    private String text;



    public dom_Comment(
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