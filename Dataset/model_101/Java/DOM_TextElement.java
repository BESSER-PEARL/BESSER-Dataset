





import java.util.List;
import java.util.ArrayList;

public class DOM_TextElement extends ASTNode {

    private String text;



    public DOM_TextElement(
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