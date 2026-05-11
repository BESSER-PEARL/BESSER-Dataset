





import java.util.List;
import java.util.ArrayList;

public class notation_Note extends Node {

    private String text;



    public notation_Note(
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