





import java.util.List;
import java.util.ArrayList;

public class model_List extends FontSupport, ColorAlternativeSupport, ItemSupport, SelectionSupport, ListSupport, Widget, BorderSupport, VerticalScrollbarSupport, ColorAlphaSupport, ColorBackgroundSupport {

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