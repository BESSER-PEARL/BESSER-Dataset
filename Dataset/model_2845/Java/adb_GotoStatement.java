





import java.util.List;
import java.util.ArrayList;

public class adb_GotoStatement extends SimpleStatement {

    private String labelId;



    public adb_GotoStatement(
        String labelId    ) {
        super(
        );
        this.labelId = labelId;
    }


    public String getLabelid() {
        return labelId;
    }

    public void setLabelid(String labelId) {
        this.labelId = labelId;
    }


}