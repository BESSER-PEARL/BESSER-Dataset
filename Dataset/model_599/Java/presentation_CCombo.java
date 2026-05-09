





import java.util.List;
import java.util.ArrayList;

public class presentation_CCombo extends Composite {

    private String textLimit;
    private String group3;
    private String selection;
    private String text;
    private String visibleItemCount;
    private String items;
    private String listVisible;
    private String editable;



    public presentation_CCombo(
        String textLimit,        String group3,        String selection,        String text,        String visibleItemCount,        String items,        String listVisible,        String editable    ) {
        super(
        );
        this.textLimit = textLimit;
        this.group3 = group3;
        this.selection = selection;
        this.text = text;
        this.visibleItemCount = visibleItemCount;
        this.items = items;
        this.listVisible = listVisible;
        this.editable = editable;
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
    public String getSelection() {
        return selection;
    }

    public void setSelection(String selection) {
        this.selection = selection;
    }
    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }
    public String getVisibleitemcount() {
        return visibleItemCount;
    }

    public void setVisibleitemcount(String visibleItemCount) {
        this.visibleItemCount = visibleItemCount;
    }
    public String getItems() {
        return items;
    }

    public void setItems(String items) {
        this.items = items;
    }
    public String getListvisible() {
        return listVisible;
    }

    public void setListvisible(String listVisible) {
        this.listVisible = listVisible;
    }
    public String getEditable() {
        return editable;
    }

    public void setEditable(String editable) {
        this.editable = editable;
    }


}