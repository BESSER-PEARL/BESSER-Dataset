





import java.util.List;
import java.util.ArrayList;

public class myDsl01_Label extends UIElement {

    private String text;



    public myDsl01_Label(
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