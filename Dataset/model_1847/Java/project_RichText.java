





import java.util.List;
import java.util.ArrayList;

public class project_RichText extends Caption, Right, Left, Center, Headline, Header, Epilog, Footer, ListItem, Details, Prolog, Summary {

    private String text;



    public project_RichText(
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