





import java.util.List;
import java.util.ArrayList;

public class prolog_String extends Term {

    private String text;



    public prolog_String(
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