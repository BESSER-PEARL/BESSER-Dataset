





import java.util.List;
import java.util.ArrayList;

public class model_Service  {

    private String application;
    private String name;
    private String stateful;



    public model_Service(
        String application,        String name,        String stateful    ) {
        this.application = application;
        this.name = name;
        this.stateful = stateful;
    }


    public String getApplication() {
        return application;
    }

    public void setApplication(String application) {
        this.application = application;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getStateful() {
        return stateful;
    }

    public void setStateful(String stateful) {
        this.stateful = stateful;
    }


}