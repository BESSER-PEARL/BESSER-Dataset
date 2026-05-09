





import java.util.List;
import java.util.ArrayList;

public class fsm_StringToStringMap  {

    private String key;
    private String value;





    private fsm_Message fsm_message;




    private fsm_FSM fsm_fsm;




    private fsm_Message fsm_message;


    public fsm_StringToStringMap(
        String key,        String value    ) {
        this.key = key;
        this.value = value;
    }


    public String getKey() {
        return key;
    }

    public void setKey(String key) {
        this.key = key;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public fsm_Message getFsm_message() {
        return fsm_message;
    }

    public void setFsm_message(fsm_Message fsm_message) {
        this.fsm_message = fsm_message;
    }
    public fsm_FSM getFsm_fsm() {
        return fsm_fsm;
    }

    public void setFsm_fsm(fsm_FSM fsm_fsm) {
        this.fsm_fsm = fsm_fsm;
    }
    public fsm_Message getFsm_message() {
        return fsm_message;
    }

    public void setFsm_message(fsm_Message fsm_message) {
        this.fsm_message = fsm_message;
    }

}