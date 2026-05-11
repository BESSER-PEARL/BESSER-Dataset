





import java.util.List;
import java.util.ArrayList;

public class diva_Expression extends DiVAModelElement {

    private String text;



    public diva_Expression(
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