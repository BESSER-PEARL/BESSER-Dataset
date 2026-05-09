





import java.util.List;
import java.util.ArrayList;

public class presentation_Text extends Scrollable {

    private String lineDelimiter;
    private String textLimit;
    private String editable;
    private String caretLocation;
    private String selectionText;
    private String doubleClickEnabled;
    private String orientation;
    private String text;
    private String selection;
    private String tabs;
    private String message;
    private String topIndex;
    private String echoChar;



    public presentation_Text(
        String lineDelimiter,        String textLimit,        String editable,        String caretLocation,        String selectionText,        String doubleClickEnabled,        String orientation,        String text,        String selection,        String tabs,        String message,        String topIndex,        String echoChar    ) {
        super(
        );
        this.lineDelimiter = lineDelimiter;
        this.textLimit = textLimit;
        this.editable = editable;
        this.caretLocation = caretLocation;
        this.selectionText = selectionText;
        this.doubleClickEnabled = doubleClickEnabled;
        this.orientation = orientation;
        this.text = text;
        this.selection = selection;
        this.tabs = tabs;
        this.message = message;
        this.topIndex = topIndex;
        this.echoChar = echoChar;
    }


    public String getLinedelimiter() {
        return lineDelimiter;
    }

    public void setLinedelimiter(String lineDelimiter) {
        this.lineDelimiter = lineDelimiter;
    }
    public String getTextlimit() {
        return textLimit;
    }

    public void setTextlimit(String textLimit) {
        this.textLimit = textLimit;
    }
    public String getEditable() {
        return editable;
    }

    public void setEditable(String editable) {
        this.editable = editable;
    }
    public String getCaretlocation() {
        return caretLocation;
    }

    public void setCaretlocation(String caretLocation) {
        this.caretLocation = caretLocation;
    }
    public String getSelectiontext() {
        return selectionText;
    }

    public void setSelectiontext(String selectionText) {
        this.selectionText = selectionText;
    }
    public String getDoubleclickenabled() {
        return doubleClickEnabled;
    }

    public void setDoubleclickenabled(String doubleClickEnabled) {
        this.doubleClickEnabled = doubleClickEnabled;
    }
    public String getOrientation() {
        return orientation;
    }

    public void setOrientation(String orientation) {
        this.orientation = orientation;
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
    public String getTabs() {
        return tabs;
    }

    public void setTabs(String tabs) {
        this.tabs = tabs;
    }
    public String getMessage() {
        return message;
    }

    public void setMessage(String message) {
        this.message = message;
    }
    public String getTopindex() {
        return topIndex;
    }

    public void setTopindex(String topIndex) {
        this.topIndex = topIndex;
    }
    public String getEchochar() {
        return echoChar;
    }

    public void setEchochar(String echoChar) {
        this.echoChar = echoChar;
    }


}