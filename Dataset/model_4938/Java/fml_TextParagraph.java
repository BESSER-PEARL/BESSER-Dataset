





import java.util.List;
import java.util.ArrayList;

public class fml_TextParagraph extends DisplayElement {

    private String Text;



    public fml_TextParagraph(
        String Text    ) {
        super(
        );
        this.Text = Text;
    }


    public String getText() {
        return Text;
    }

    public void setText(String Text) {
        this.Text = Text;
    }


}