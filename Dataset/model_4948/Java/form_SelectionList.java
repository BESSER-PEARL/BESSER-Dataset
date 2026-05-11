





import java.util.List;
import java.util.ArrayList;

public class form_SelectionList extends Editable {

    private boolean multiple;



    public form_SelectionList(
        boolean multiple    ) {
        super(
        );
        this.multiple = multiple;
    }


    public boolean getMultiple() {
        return multiple;
    }

    public void setMultiple(boolean multiple) {
        this.multiple = multiple;
    }


}