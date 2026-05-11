





import java.util.List;
import java.util.ArrayList;

public class core_call_SafiCall extends ThreadSensitive, PlatformDisposition {

    private String uuid;
    private String name;



    public core_call_SafiCall(
        String uuid,        String name    ) {
        super(
        );
        this.uuid = uuid;
        this.name = name;
    }


    public String getUuid() {
        return uuid;
    }

    public void setUuid(String uuid) {
        this.uuid = uuid;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}