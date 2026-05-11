





import java.util.List;
import java.util.ArrayList;

public class model_Pick extends Activity {

    private String createInstance;





    private List<model_OnMessage> model_onmessages;




    private List<model_OnAlarm> model_onalarms;


    public model_Pick(
        String createInstance    ) {
        super(
        );
        this.createInstance = createInstance;
        this.model_onmessages = new ArrayList<>();
        this.model_onalarms = new ArrayList<>();
    }

    public model_Pick(
        String createInstance        ArrayList<model_OnMessage> model_onmessages,        ArrayList<model_OnAlarm> model_onalarms    ) {
        this.createInstance = createInstance;
        this.model_onmessages = model_onmessages;
        this.model_onalarms = model_onalarms;
    }

    public String getCreateinstance() {
        return createInstance;
    }

    public void setCreateinstance(String createInstance) {
        this.createInstance = createInstance;
    }

    public List<model_OnMessage> getModel_onmessages() {
        return model_onmessages;
    }

    public void addModel_onmessage(Model_onmessage model_onmessage) {
        this.model_onmessages.add(model_onmessage);
    }
    public List<model_OnAlarm> getModel_onalarms() {
        return model_onalarms;
    }

    public void addModel_onalarm(Model_onalarm model_onalarm) {
        this.model_onalarms.add(model_onalarm);
    }

}