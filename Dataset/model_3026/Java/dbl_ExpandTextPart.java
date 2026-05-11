





import java.util.List;
import java.util.ArrayList;

public class dbl_ExpandTextPart extends ExpansionPart {

    private String text;



    public dbl_ExpandTextPart(
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