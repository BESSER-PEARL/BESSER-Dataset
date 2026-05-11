





import java.util.List;
import java.util.ArrayList;

public class model_Table extends ListSupport, SelectionSupport, ColorAlphaSupport, BorderSupport, Widget, ColorBackgroundSupport, TextLinksSupport, VerticalScrollbarSupport, TextAlignmentSupport, ColorAlternativeSupport, FontSupport {

    private boolean verticalLines;
    private boolean header;



    public model_Table(
        boolean verticalLines,        boolean header    ) {
        super(
        );
        this.verticalLines = verticalLines;
        this.header = header;
    }


    public boolean getVerticallines() {
        return verticalLines;
    }

    public void setVerticallines(boolean verticalLines) {
        this.verticalLines = verticalLines;
    }
    public boolean getHeader() {
        return header;
    }

    public void setHeader(boolean header) {
        this.header = header;
    }


}