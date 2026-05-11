





import java.util.List;
import java.util.ArrayList;

public class html_SelectionList extends Editable {

    private boolean multiple;



    public html_SelectionList(
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