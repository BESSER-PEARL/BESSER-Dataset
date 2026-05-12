





import java.util.List;
import java.util.ArrayList;

public class xdoc_Todo extends MarkupInCode, MarkUp {

    private String text;



    public xdoc_Todo(
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