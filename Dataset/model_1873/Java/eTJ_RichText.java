





import java.util.List;
import java.util.ArrayList;

public class eTJ_RichText extends ListItem, Prolog, Left, Summary, Headline, Epilog, Right, Details, Header, Center, Caption, Footer {

    private String text;



    public eTJ_RichText(
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