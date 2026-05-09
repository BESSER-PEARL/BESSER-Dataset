





import java.util.List;
import java.util.ArrayList;

public class dom_XmlTextFragment extends XmlFragment {

    private String text;



    public dom_XmlTextFragment(
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