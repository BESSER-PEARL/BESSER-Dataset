





import java.util.List;
import java.util.ArrayList;

public class pp2_SingleQuotedString extends StringExpression, IQuotedString {

    private String text;



    public pp2_SingleQuotedString(
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