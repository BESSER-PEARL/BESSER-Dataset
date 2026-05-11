





import java.util.List;
import java.util.ArrayList;

public class swt_Text extends Control {

    private String message;
    private int tabs;
    private boolean editable;
    private String echoChar;
    private String text;
    private int topIndex;
    private int textLimit;
    private String multiplicityStyle;
    private String selection;



    public swt_Text(
        String message,        int tabs,        boolean editable,        String echoChar,        String text,        int topIndex,        int textLimit,        String multiplicityStyle,        String selection    ) {
        super(
        );
        this.message = message;
        this.tabs = tabs;
        this.editable = editable;
        this.echoChar = echoChar;
        this.text = text;
        this.topIndex = topIndex;
        this.textLimit = textLimit;
        this.multiplicityStyle = multiplicityStyle;
        this.selection = selection;
    }


    public String getMessage() {
        return message;
    }

    public void setMessage(String message) {
        this.message = message;
    }
    public int getTabs() {
        return tabs;
    }

    public void setTabs(int tabs) {
        this.tabs = tabs;
    }
    public boolean getEditable() {
        return editable;
    }

    public void setEditable(boolean editable) {
        this.editable = editable;
    }
    public String getEchochar() {
        return echoChar;
    }

    public void setEchochar(String echoChar) {
        this.echoChar = echoChar;
    }
    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }
    public int getTopindex() {
        return topIndex;
    }

    public void setTopindex(int topIndex) {
        this.topIndex = topIndex;
    }
    public int getTextlimit() {
        return textLimit;
    }

    public void setTextlimit(int textLimit) {
        this.textLimit = textLimit;
    }
    public String getMultiplicitystyle() {
        return multiplicityStyle;
    }

    public void setMultiplicitystyle(String multiplicityStyle) {
        this.multiplicityStyle = multiplicityStyle;
    }
    public String getSelection() {
        return selection;
    }

    public void setSelection(String selection) {
        this.selection = selection;
    }


}