





import java.util.List;
import java.util.ArrayList;

public class db_config_Saflet extends ServerResource {

    private String code;
    private String subsystemId;



    public db_config_Saflet(
        String code,        String subsystemId    ) {
        super(
        );
        this.code = code;
        this.subsystemId = subsystemId;
    }


    public String getCode() {
        return code;
    }

    public void setCode(String code) {
        this.code = code;
    }
    public String getSubsystemid() {
        return subsystemId;
    }

    public void setSubsystemid(String subsystemId) {
        this.subsystemId = subsystemId;
    }


}