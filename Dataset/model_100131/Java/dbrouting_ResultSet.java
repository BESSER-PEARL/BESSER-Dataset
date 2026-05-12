





import java.util.List;
import java.util.ArrayList;

public class dbrouting_ResultSet  {

    private String name;
    private String timeToLive;
    private String scope;





    private dbrouting_Executor dbrouting_executor;


    public dbrouting_ResultSet(
        String name,        String timeToLive,        String scope    ) {
        this.name = name;
        this.timeToLive = timeToLive;
        this.scope = scope;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getTimetolive() {
        return timeToLive;
    }

    public void setTimetolive(String timeToLive) {
        this.timeToLive = timeToLive;
    }
    public String getScope() {
        return scope;
    }

    public void setScope(String scope) {
        this.scope = scope;
    }

    public dbrouting_Executor getDbrouting_executor() {
        return dbrouting_executor;
    }

    public void setDbrouting_executor(dbrouting_Executor dbrouting_executor) {
        this.dbrouting_executor = dbrouting_executor;
    }

}