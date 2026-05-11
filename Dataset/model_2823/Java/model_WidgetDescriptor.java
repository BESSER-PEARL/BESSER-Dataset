





import java.util.List;
import java.util.ArrayList;

public class model_WidgetDescriptor  {

    private boolean textWrappable;
    private String resizeMode;
    private boolean textEditable;
    private int textLines;
    private boolean textCentered;
    private String typeName;





    private model_Widget model_widget;


    public model_WidgetDescriptor(
        boolean textWrappable,        String resizeMode,        boolean textEditable,        int textLines,        boolean textCentered,        String typeName    ) {
        this.textWrappable = textWrappable;
        this.resizeMode = resizeMode;
        this.textEditable = textEditable;
        this.textLines = textLines;
        this.textCentered = textCentered;
        this.typeName = typeName;
    }


    public boolean getTextwrappable() {
        return textWrappable;
    }

    public void setTextwrappable(boolean textWrappable) {
        this.textWrappable = textWrappable;
    }
    public String getResizemode() {
        return resizeMode;
    }

    public void setResizemode(String resizeMode) {
        this.resizeMode = resizeMode;
    }
    public boolean getTexteditable() {
        return textEditable;
    }

    public void setTexteditable(boolean textEditable) {
        this.textEditable = textEditable;
    }
    public int getTextlines() {
        return textLines;
    }

    public void setTextlines(int textLines) {
        this.textLines = textLines;
    }
    public boolean getTextcentered() {
        return textCentered;
    }

    public void setTextcentered(boolean textCentered) {
        this.textCentered = textCentered;
    }
    public String getTypename() {
        return typeName;
    }

    public void setTypename(String typeName) {
        this.typeName = typeName;
    }

    public model_Widget getModel_widget() {
        return model_widget;
    }

    public void setModel_widget(model_Widget model_widget) {
        this.model_widget = model_widget;
    }

}