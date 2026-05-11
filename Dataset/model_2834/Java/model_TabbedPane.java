





import java.util.List;
import java.util.ArrayList;

public class model_TabbedPane extends SkinSupport, Widget, VerticalScrollbarSupport, ColorBackgroundSupport, FontSupport, ColorAlphaSupport, ItemSupport, SelectionSupport {

    private String position;



    public model_TabbedPane(
        String position    ) {
        super(
        );
        this.position = position;
    }


    public String getPosition() {
        return position;
    }

    public void setPosition(String position) {
        this.position = position;
    }


}