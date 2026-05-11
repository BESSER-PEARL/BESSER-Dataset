





import java.util.List;
import java.util.ArrayList;

public class mprologTermReference_QuotedAtom extends Term {

    private String text;



    public mprologTermReference_QuotedAtom(
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