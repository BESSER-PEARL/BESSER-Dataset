





import java.util.List;
import java.util.ArrayList;

public class tortugaDSL_DRAW_STRING extends DRAWING_SENTENCE {

    private String text;



    public tortugaDSL_DRAW_STRING(
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