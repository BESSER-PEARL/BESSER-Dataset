





import java.util.List;
import java.util.ArrayList;

public class ast_TextElement extends ASTNode, IDocElement {

    private String text;



    public ast_TextElement(
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