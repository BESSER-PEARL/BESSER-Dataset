





import java.util.List;
import java.util.ArrayList;

public class documentation_ListItem extends TextFragmentContainer {

    private String text;



    public documentation_ListItem(
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