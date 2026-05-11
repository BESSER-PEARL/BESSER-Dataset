





import java.util.List;
import java.util.ArrayList;

public class model_TabbedPane extends ItemSupport, SelectionSupport, ColorAlphaSupport, SkinSupport, Widget, ColorBackgroundSupport, VerticalScrollbarSupport, FontSupport {

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