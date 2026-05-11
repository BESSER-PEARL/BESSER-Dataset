





import java.util.List;
import java.util.ArrayList;

public class model_List extends ListSupport, BorderSupport, ColorAlternativeSupport, Widget, ColorBackgroundSupport, VerticalScrollbarSupport, FontSupport, ColorAlphaSupport, ItemSupport, SelectionSupport {

    private boolean header;



    public model_List(
        boolean header    ) {
        super(
        );
        this.header = header;
    }


    public boolean getHeader() {
        return header;
    }

    public void setHeader(boolean header) {
        this.header = header;
    }


}