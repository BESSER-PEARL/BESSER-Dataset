





import java.util.List;
import java.util.ArrayList;

public class model_Text extends TextAlignmentSupport, TextLinksSupport, LineHeightSupport, LinkSupport, Widget, FontSupport, ColorForegroundSupport {

    private boolean dummyText;



    public model_Text(
        boolean dummyText    ) {
        super(
        );
        this.dummyText = dummyText;
    }


    public boolean getDummytext() {
        return dummyText;
    }

    public void setDummytext(boolean dummyText) {
        this.dummyText = dummyText;
    }


}