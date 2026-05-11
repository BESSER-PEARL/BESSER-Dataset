





import java.util.List;
import java.util.ArrayList;

public class model_VerticalScrollbarSupport extends ValueSupport {

    private boolean verticalScrollbar;



    public model_VerticalScrollbarSupport(
        boolean verticalScrollbar    ) {
        super(
        );
        this.verticalScrollbar = verticalScrollbar;
    }


    public boolean getVerticalscrollbar() {
        return verticalScrollbar;
    }

    public void setVerticalscrollbar(boolean verticalScrollbar) {
        this.verticalScrollbar = verticalScrollbar;
    }


}