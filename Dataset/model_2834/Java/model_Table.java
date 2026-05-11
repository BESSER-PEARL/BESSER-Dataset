





import java.util.List;
import java.util.ArrayList;

public class model_Table extends TextLinksSupport, TextAlignmentSupport, ListSupport, BorderSupport, ColorAlternativeSupport, DoubleClickSupport, TextInputSupport, Widget, VerticalScrollbarSupport, ColorBackgroundSupport, FontSupport, ClickSupport, ColorAlphaSupport, SelectionSupport {

    private boolean header;
    private boolean verticalLines;



    public model_Table(
        boolean header,        boolean verticalLines    ) {
        super(
        );
        this.header = header;
        this.verticalLines = verticalLines;
    }


    public boolean getHeader() {
        return header;
    }

    public void setHeader(boolean header) {
        this.header = header;
    }
    public boolean getVerticallines() {
        return verticalLines;
    }

    public void setVerticallines(boolean verticalLines) {
        this.verticalLines = verticalLines;
    }


}