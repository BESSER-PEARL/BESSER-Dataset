





import java.util.List;
import java.util.ArrayList;

public class swt_Button extends Labeled, Control {

    private String arrowStyle;
    private boolean selection;
    private String buttonStyle;



    public swt_Button(
        String arrowStyle,        boolean selection,        String buttonStyle    ) {
        super(
        );
        this.arrowStyle = arrowStyle;
        this.selection = selection;
        this.buttonStyle = buttonStyle;
    }


    public String getArrowstyle() {
        return arrowStyle;
    }

    public void setArrowstyle(String arrowStyle) {
        this.arrowStyle = arrowStyle;
    }
    public boolean getSelection() {
        return selection;
    }

    public void setSelection(boolean selection) {
        this.selection = selection;
    }
    public String getButtonstyle() {
        return buttonStyle;
    }

    public void setButtonstyle(String buttonStyle) {
        this.buttonStyle = buttonStyle;
    }


}