





import java.util.List;
import java.util.ArrayList;

public class gmfgraph_Label extends Figure {

    private String text;



    public gmfgraph_Label(
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