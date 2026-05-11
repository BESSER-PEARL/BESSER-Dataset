





import java.util.List;
import java.util.ArrayList;

public class spinefm_ProcessModel_LocalContext extends Context {






    private List<Configuration> configurations;


    public spinefm_ProcessModel_LocalContext(
    ) {
        super(
        );
        this.configurations = new ArrayList<>();
    }

    public spinefm_ProcessModel_LocalContext(
        ArrayList<Configuration> configurations    ) {
        this.configurations = configurations;
    }


    public List<Configuration> getConfigurations() {
        return configurations;
    }

    public void addConfiguration(Configuration configuration) {
        this.configurations.add(configuration);
    }

}