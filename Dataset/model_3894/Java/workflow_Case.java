





import java.util.List;
import java.util.ArrayList;

public class workflow_Case  {

    private String client;
    private boolean started;
    private String id;
    private boolean finished;



    public workflow_Case(
        String client,        boolean started,        String id,        boolean finished    ) {
        this.client = client;
        this.started = started;
        this.id = id;
        this.finished = finished;
    }


    public String getClient() {
        return client;
    }

    public void setClient(String client) {
        this.client = client;
    }
    public boolean getStarted() {
        return started;
    }

    public void setStarted(boolean started) {
        this.started = started;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public boolean getFinished() {
        return finished;
    }

    public void setFinished(boolean finished) {
        this.finished = finished;
    }


}