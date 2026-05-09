





import java.util.List;
import java.util.ArrayList;

public class presentation_Combo extends Composite {

    private String group3;
    private String textLimit;
    private String items;
    private String visibleItemCount;
    private String orientation;
    private String listVisible;
    private String text;
    private String selection;



    public presentation_Combo(
        String group3,        String textLimit,        String items,        String visibleItemCount,        String orientation,        String listVisible,        String text,        String selection    ) {
        super(
        );
        this.group3 = group3;
        this.textLimit = textLimit;
        this.items = items;
        this.visibleItemCount = visibleItemCount;
        this.orientation = orientation;
        this.listVisible = listVisible;
        this.text = text;
        this.selection = selection;
    }


    public String getGroup3() {
        return group3;
    }

    public void setGroup3(String group3) {
        this.group3 = group3;
    }
    public String getTextlimit() {
        return textLimit;
    }

    public void setTextlimit(String textLimit) {
        this.textLimit = textLimit;
    }
    public String getItems() {
        return items;
    }

    public void setItems(String items) {
        this.items = items;
    }
    public String getVisibleitemcount() {
        return visibleItemCount;
    }

    public void setVisibleitemcount(String visibleItemCount) {
        this.visibleItemCount = visibleItemCount;
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
    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }
    public String getSelection() {
        return selection;
    }

    public void setSelection(String selection) {
        this.selection = selection;
    }


}