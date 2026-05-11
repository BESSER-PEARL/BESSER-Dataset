





import java.util.List;
import java.util.ArrayList;

public class behavior_ObservedUseCaseExecution extends AbstractUseCaseExecution {

    private String startTime;
    private String endTime;





    private behavior_Session behavior_session;


    public behavior_ObservedUseCaseExecution(
        String startTime,        String endTime    ) {
        super(
        );
        this.startTime = startTime;
        this.endTime = endTime;
    }


    public String getStarttime() {
        return startTime;
    }

    public void setStarttime(String startTime) {
        this.startTime = startTime;
    }
    public String getEndtime() {
        return endTime;
    }

    public void setEndtime(String endTime) {
        this.endTime = endTime;
    }

    public behavior_Session getBehavior_session() {
        return behavior_session;
    }

    public void setBehavior_session(behavior_Session behavior_session) {
        this.behavior_session = behavior_session;
    }

}