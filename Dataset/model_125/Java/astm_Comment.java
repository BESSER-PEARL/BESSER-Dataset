





import java.util.List;
import java.util.ArrayList;

public class astm_Comment extends PreprocessorElement {

    private String text;



    public astm_Comment(
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