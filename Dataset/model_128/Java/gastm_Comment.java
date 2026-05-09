





import java.util.List;
import java.util.ArrayList;

public class gastm_Comment extends PreprocessorElement {

    private String text;



    public gastm_Comment(
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