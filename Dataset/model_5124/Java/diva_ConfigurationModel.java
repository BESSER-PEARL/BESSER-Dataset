





import java.util.List;
import java.util.ArrayList;

public class diva_ConfigurationModel extends Visitable {






    private List<diva_SuitableConfiguration> diva_suitableconfigurations;


    public diva_ConfigurationModel(
    ) {
        super(
        );
        this.diva_suitableconfigurations = new ArrayList<>();
    }

    public diva_ConfigurationModel(
        ArrayList<diva_SuitableConfiguration> diva_suitableconfigurations    ) {
        this.diva_suitableconfigurations = diva_suitableconfigurations;
    }


    public List<diva_SuitableConfiguration> getDiva_suitableconfigurations() {
        return diva_suitableconfigurations;
    }

    public void addDiva_suitableconfiguration(Diva_suitableconfiguration diva_suitableconfiguration) {
        this.diva_suitableconfigurations.add(diva_suitableconfiguration);
    }

}