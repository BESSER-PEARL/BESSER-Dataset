





import java.util.List;
import java.util.ArrayList;

public class viewpoint_tool_DialogVariable extends AbstractVariable {

    private String dialogPrompt;



    public viewpoint_tool_DialogVariable(
        String dialogPrompt    ) {
        super(
        );
        this.dialogPrompt = dialogPrompt;
    }


    public String getDialogprompt() {
        return dialogPrompt;
    }

    public void setDialogprompt(String dialogPrompt) {
        this.dialogPrompt = dialogPrompt;
    }


}