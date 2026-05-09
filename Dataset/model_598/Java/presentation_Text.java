





import java.util.List;
import java.util.ArrayList;

public class presentation_Text extends Scrollable {

    private String selectionText;
    private String text;
    private String message;
    private String selection;
    private String doubleClickEnabled;
    private String editable;
    private String echoChar;
    private String orientation;
    private String textLimit;
    private String caretLocation;
    private String topIndex;
    private String tabs;
    private String lineDelimiter;



    public presentation_Text(
        String selectionText,        String text,        String message,        String selection,        String doubleClickEnabled,        String editable,        String echoChar,        String orientation,        String textLimit,        String caretLocation,        String topIndex,        String tabs,        String lineDelimiter    ) {
        super(
        );
        this.selectionText = selectionText;
        this.text = text;
        this.message = message;
        this.selection = selection;
        this.doubleClickEnabled = doubleClickEnabled;
        this.editable = editable;
        this.echoChar = echoChar;
        this.orientation = orientation;
        this.textLimit = textLimit;
        this.caretLocation = caretLocation;
        this.topIndex = topIndex;
        this.tabs = tabs;
        this.lineDelimiter = lineDelimiter;
    }


    public String getSelectiontext() {
        return selectionText;
    }

    public void setSelectiontext(String selectionText) {
        this.selectionText = selectionText;
    }
    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }
    public String getMessage() {
        return message;
    }

    public void setMessage(String message) {
        this.message = message;
    }
    public String getSelection() {
        return selection;
    }

    public void setSelection(String selection) {
        this.selection = selection;
    }
    public String getDoubleclickenabled() {
        return doubleClickEnabled;
    }

    public void setDoubleclickenabled(String doubleClickEnabled) {
        this.doubleClickEnabled = doubleClickEnabled;
    }
    public String getEditable() {
        return editable;
    }

    public void setEditable(String editable) {
        this.editable = editable;
    }
    public String getEchochar() {
        return echoChar;
    }

    public void setEchochar(String echoChar) {
        this.echoChar = echoChar;
    }
    public String getOrientation() {
        return orientation;
    }

    public void setOrientation(String orientation) {
        this.orientation = orientation;
    }
    public String getTextlimit() {
        return textLimit;
    }

    public void setTextlimit(String textLimit) {
        this.textLimit = textLimit;
    }
    public String getCaretlocation() {
        return caretLocation;
    }

    public void setCaretlocation(String caretLocation) {
        this.caretLocation = caretLocation;
    }
    public String getTopindex() {
        return topIndex;
    }

    public void setTopindex(String topIndex) {
        this.topIndex = topIndex;
    }
    public String getTabs() {
        return tabs;
    }

    public void setTabs(String tabs) {
        this.tabs = tabs;
    }
    public String getLinedelimiter() {
        return lineDelimiter;
    }

    public void setLinedelimiter(String lineDelimiter) {
        this.lineDelimiter = lineDelimiter;
    }


}