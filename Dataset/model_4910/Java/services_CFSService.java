





import java.util.List;
import java.util.ArrayList;

public class services_CFSService extends Service {

    private String provider;
    private String scenario;



    public services_CFSService(
        String provider,        String scenario    ) {
        super(
        );
        this.provider = provider;
        this.scenario = scenario;
    }


    public String getProvider() {
        return provider;
    }

    public void setProvider(String provider) {
        this.provider = provider;
    }
    public String getScenario() {
        return scenario;
    }

    public void setScenario(String scenario) {
        this.scenario = scenario;
    }


}