





import java.util.List;
import java.util.ArrayList;

public class webapp_FormButton extends Control {

    private String text;



    public webapp_FormButton(
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