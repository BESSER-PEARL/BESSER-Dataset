





import java.util.List;
import java.util.ArrayList;

public class swt_AbstractList extends Control {

    private int selectionIndex;
    private String items;



    public swt_AbstractList(
        int selectionIndex,        String items    ) {
        super(
        );
        this.selectionIndex = selectionIndex;
        this.items = items;
    }


    public int getSelectionindex() {
        return selectionIndex;
    }

    public void setSelectionindex(int selectionIndex) {
        this.selectionIndex = selectionIndex;
    }
    public String getItems() {
        return items;
    }

    public void setItems(String items) {
        this.items = items;
    }


}