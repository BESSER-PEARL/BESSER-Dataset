





import java.util.List;
import java.util.ArrayList;

public class model_WidgetDescriptor  {

    private int textLines;
    private boolean textCentered;
    private boolean textWrappable;
    private boolean textEditable;
    private String resizeMode;
    private String typeName;





    private model_Widget model_widget;


    public model_WidgetDescriptor(
        int textLines,        boolean textCentered,        boolean textWrappable,        boolean textEditable,        String resizeMode,        String typeName    ) {
        this.textLines = textLines;
        this.textCentered = textCentered;
        this.textWrappable = textWrappable;
        this.textEditable = textEditable;
        this.resizeMode = resizeMode;
        this.typeName = typeName;
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
    public boolean getTextwrappable() {
        return textWrappable;
    }

    public void setTextwrappable(boolean textWrappable) {
        this.textWrappable = textWrappable;
    }
    public boolean getTexteditable() {
        return textEditable;
    }

    public void setTexteditable(boolean textEditable) {
        this.textEditable = textEditable;
    }
    public String getResizemode() {
        return resizeMode;
    }

    public void setResizemode(String resizeMode) {
        this.resizeMode = resizeMode;
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