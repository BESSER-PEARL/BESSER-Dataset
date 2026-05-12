





import java.util.List;
import java.util.ArrayList;

public class stateMachine_RemoveRecord extends IvrAction {

    private String recordId;



    public stateMachine_RemoveRecord(
        String recordId    ) {
        super(
        );
        this.recordId = recordId;
    }


    public String getRecordid() {
        return recordId;
    }

    public void setRecordid(String recordId) {
        this.recordId = recordId;
    }


}