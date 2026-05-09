





import java.util.List;
import java.util.ArrayList;

public class presentation_Group extends Composite {

    private String text;



    public presentation_Group(
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