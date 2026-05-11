





import java.util.List;
import java.util.ArrayList;

public class classLayout2Frontend_Views_InputText extends Input {

    private boolean multiline;



    public classLayout2Frontend_Views_InputText(
        boolean multiline    ) {
        super(
        );
        this.multiline = multiline;
    }


    public boolean getMultiline() {
        return multiline;
    }

    public void setMultiline(boolean multiline) {
        this.multiline = multiline;
    }


}