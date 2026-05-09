





import java.util.List;
import java.util.ArrayList;

public class presentation_Combo extends Composite {

    private String items;
    private String selection;
    private String visibleItemCount;
    private String text;
    private String textLimit;
    private String group3;
    private String orientation;
    private String listVisible;



    public presentation_Combo(
        String items,        String selection,        String visibleItemCount,        String text,        String textLimit,        String group3,        String orientation,        String listVisible    ) {
        super(
        );
        this.items = items;
        this.selection = selection;
        this.visibleItemCount = visibleItemCount;
        this.text = text;
        this.textLimit = textLimit;
        this.group3 = group3;
        this.orientation = orientation;
        this.listVisible = listVisible;
    }


    public String getItems() {
        return items;
    }

    public void setItems(String items) {
        this.items = items;
    }
    public String getSelection() {
        return selection;
    }

    public void setSelection(String selection) {
        this.selection = selection;
    }
    public String getVisibleitemcount() {
        return visibleItemCount;
    }

    public void setVisibleitemcount(String visibleItemCount) {
        this.visibleItemCount = visibleItemCount;
    }
    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }
    public String getTextlimit() {
        return textLimit;
    }

    public void setTextlimit(String textLimit) {
        this.textLimit = textLimit;
    }
    public String getGroup3() {
        return group3;
    }

    public void setGroup3(String group3) {
        this.group3 = group3;
    }
    public String getOrientation() {
        return orientation;
    }

    public void setOrientation(String orientation) {
        this.orientation = orientation;
    }
    public String getListvisible() {
        return listVisible;
    }

    public void setListvisible(String listVisible) {
        this.listVisible = listVisible;
    }


}