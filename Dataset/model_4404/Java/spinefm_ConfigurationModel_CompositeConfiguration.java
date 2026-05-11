





import java.util.List;
import java.util.ArrayList;

public class spinefm_ConfigurationModel_CompositeConfiguration  {

    private String name;





    private List<Configuration> configurations;


    public spinefm_ConfigurationModel_CompositeConfiguration(
        String name    ) {
        this.name = name;
        this.configurations = new ArrayList<>();
    }

    public spinefm_ConfigurationModel_CompositeConfiguration(
        String name        ArrayList<Configuration> configurations    ) {
        this.name = name;
        this.configurations = configurations;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<Configuration> getConfigurations() {
        return configurations;
    }

    public void addConfiguration(Configuration configuration) {
        this.configurations.add(configuration);
    }

}