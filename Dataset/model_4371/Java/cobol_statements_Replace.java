





import java.util.List;
import java.util.ArrayList;

public class cobol_statements_Replace extends Statement {

    private boolean replaceSwitch;



    public cobol_statements_Replace(
        boolean replaceSwitch    ) {
        super(
        );
        this.replaceSwitch = replaceSwitch;
    }


    public boolean getReplaceswitch() {
        return replaceSwitch;
    }

    public void setReplaceswitch(boolean replaceSwitch) {
        this.replaceSwitch = replaceSwitch;
    }


}