





import java.util.List;
import java.util.ArrayList;

public class form_List extends PageElement {

    private boolean ordered;



    public form_List(
        boolean ordered    ) {
        super(
        );
        this.ordered = ordered;
    }


    public boolean getOrdered() {
        return ordered;
    }

    public void setOrdered(boolean ordered) {
        this.ordered = ordered;
    }


}