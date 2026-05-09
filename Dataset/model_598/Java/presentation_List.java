





import java.util.List;
import java.util.ArrayList;

public class presentation_List extends Scrollable {

    private String topIndex;
    private String selectionIndices;
    private String selection;
    private String items;
    private String group2;





    private presentation_ListViewer presentation_listviewer;


    public presentation_List(
        String topIndex,        String selectionIndices,        String selection,        String items,        String group2    ) {
        super(
        );
        this.topIndex = topIndex;
        this.selectionIndices = selectionIndices;
        this.selection = selection;
        this.items = items;
        this.group2 = group2;
    }


    public String getTopindex() {
        return topIndex;
    }

    public void setTopindex(String topIndex) {
        this.topIndex = topIndex;
    }
    public String getSelectionindices() {
        return selectionIndices;
    }

    public void setSelectionindices(String selectionIndices) {
        this.selectionIndices = selectionIndices;
    }
    public String getSelection() {
        return selection;
    }

    public void setSelection(String selection) {
        this.selection = selection;
    }
    public String getItems() {
        return items;
    }

    public void setItems(String items) {
        this.items = items;
    }
    public String getGroup2() {
        return group2;
    }

    public void setGroup2(String group2) {
        this.group2 = group2;
    }

    public presentation_ListViewer getPresentation_listviewer() {
        return presentation_listviewer;
    }

    public void setPresentation_listviewer(presentation_ListViewer presentation_listviewer) {
        this.presentation_listviewer = presentation_listviewer;
    }

}