





import java.util.List;
import java.util.ArrayList;

public class petrinet_Identity extends Attribute {

    private String text;



    public petrinet_Identity(
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