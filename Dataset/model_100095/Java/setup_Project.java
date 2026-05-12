





import java.util.List;
import java.util.ArrayList;

public class setup_Project extends ConfigurableItem {

    private String label;
    private String name;





    private setup_Configuration setup_configuration;




    private setup_Configuration setup_configuration;


    public setup_Project(
        String label,        String name    ) {
        super(
        );
        this.label = label;
        this.name = name;
    }


    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public setup_Configuration getSetup_configuration() {
        return setup_configuration;
    }

    public void setSetup_configuration(setup_Configuration setup_configuration) {
        this.setup_configuration = setup_configuration;
    }
    public setup_Configuration getSetup_configuration() {
        return setup_configuration;
    }

    public void setSetup_configuration(setup_Configuration setup_configuration) {
        this.setup_configuration = setup_configuration;
    }

}