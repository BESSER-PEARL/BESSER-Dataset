





import java.util.List;
import java.util.ArrayList;

public class haxe_HaxeTextElement extends HaxeASTNode {

    private String text;



    public haxe_HaxeTextElement(
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