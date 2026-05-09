





import java.util.List;
import java.util.ArrayList;

public class JDTAST_TextElement extends ASTNode {

    private String text;



    public JDTAST_TextElement(
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