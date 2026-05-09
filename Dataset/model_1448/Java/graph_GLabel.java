





import java.util.List;
import java.util.ArrayList;

public class graph_GLabel extends GAlignable, GShapeElement, GEdgeLayoutable {

    private String text;



    public graph_GLabel(
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