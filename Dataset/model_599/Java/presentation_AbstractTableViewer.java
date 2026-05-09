





import java.util.List;
import java.util.ArrayList;

public class presentation_AbstractTableViewer extends ColumnViewer {

    private String itemCount;



    public presentation_AbstractTableViewer(
        String itemCount    ) {
        super(
        );
        this.itemCount = itemCount;
    }


    public String getItemcount() {
        return itemCount;
    }

    public void setItemcount(String itemCount) {
        this.itemCount = itemCount;
    }


}