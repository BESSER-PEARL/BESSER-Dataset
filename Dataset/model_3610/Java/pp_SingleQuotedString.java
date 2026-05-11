





import java.util.List;
import java.util.ArrayList;

public class pp_SingleQuotedString extends IQuotedString, StringExpression {

    private String text;



    public pp_SingleQuotedString(
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