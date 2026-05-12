





import java.util.List;
import java.util.ArrayList;

public class stateMachine_Recorderd extends IVREvent {

    private String recordId;



    public stateMachine_Recorderd(
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