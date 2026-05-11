





import java.util.List;
import java.util.ArrayList;

public class pp_VerbatimTE extends TextExpression {

    private String text;



    public pp_VerbatimTE(
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