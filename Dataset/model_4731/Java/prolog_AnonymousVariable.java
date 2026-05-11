





import java.util.List;
import java.util.ArrayList;

public class prolog_AnonymousVariable extends Term {

    private String text;



    public prolog_AnonymousVariable(
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