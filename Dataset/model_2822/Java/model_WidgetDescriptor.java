





import java.util.List;
import java.util.ArrayList;

public class model_WidgetDescriptor  {

    private int textLines;
    private String typeName;
    private boolean textEditable;
    private boolean textWrappable;
    private String resizeMode;
    private boolean textCentered;





    private model_Widget model_widget;


    public model_WidgetDescriptor(
        int textLines,        String typeName,        boolean textEditable,        boolean textWrappable,        String resizeMode,        boolean textCentered    ) {
        this.textLines = textLines;
        this.typeName = typeName;
        this.textEditable = textEditable;
        this.textWrappable = textWrappable;
        this.resizeMode = resizeMode;
        this.textCentered = textCentered;
    }


    public int getTextlines() {
        return textLines;
    }

    public void setTextlines(int textLines) {
        this.textLines = textLines;
    }
    public String getTypename() {
        return typeName;
    }

    public void setTypename(String typeName) {
        this.typeName = typeName;
    }
    public boolean getTexteditable() {
        return textEditable;
    }

    public void setTexteditable(boolean textEditable) {
        this.textEditable = textEditable;
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
    public boolean getTextcentered() {
        return textCentered;
    }

    public void setTextcentered(boolean textCentered) {
        this.textCentered = textCentered;
    }

    public model_Widget getModel_widget() {
        return model_widget;
    }

    public void setModel_widget(model_Widget model_widget) {
        this.model_widget = model_widget;
    }

}