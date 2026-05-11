





import java.util.List;
import java.util.ArrayList;

public class swt_Group extends Composite {

    private String text;



    public swt_Group(
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