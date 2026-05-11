





import java.util.List;
import java.util.ArrayList;

public class model_List extends ItemSupport, ListSupport, SelectionSupport, ColorAlphaSupport, BorderSupport, Widget, ColorBackgroundSupport, VerticalScrollbarSupport, ColorAlternativeSupport, FontSupport {

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