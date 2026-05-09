





import java.util.List;
import java.util.ArrayList;

public class capellacommon_TimeEvent extends StateEvent {

    private String time;
    private String kind;



    public capellacommon_TimeEvent(
        String time,        String kind    ) {
        super(
        );
        this.time = time;
        this.kind = kind;
    }


    public String getTime() {
        return time;
    }

    public void setTime(String time) {
        this.time = time;
    }
    public String getKind() {
        return kind;
    }

    public void setKind(String kind) {
        this.kind = kind;
    }


}