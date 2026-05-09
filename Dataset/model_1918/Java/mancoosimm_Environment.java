





import java.util.List;
import java.util.ArrayList;

public class mancoosimm_Environment extends NamedElement {






    private mancoosimm_Alternative mancoosimm_alternative;




    private mancoosimm_SkeeperCatalog mancoosimm_skeepercatalog;




    private List<mancoosimm_Alternative> mancoosimm_alternatives;




    private mancoosimm_Configuration mancoosimm_configuration;




    private mancoosimm_SkeeperCatalog mancoosimm_skeepercatalog;




    private mancoosimm_Configuration mancoosimm_configuration;


    public mancoosimm_Environment(
    ) {
        super(
        );
        this.mancoosimm_alternatives = new ArrayList<>();
    }

    public mancoosimm_Environment(
        ArrayList<mancoosimm_Alternative> mancoosimm_alternatives    ) {
        this.mancoosimm_alternatives = mancoosimm_alternatives;
    }


    public mancoosimm_Alternative getMancoosimm_alternative() {
        return mancoosimm_alternative;
    }

    public void setMancoosimm_alternative(mancoosimm_Alternative mancoosimm_alternative) {
        this.mancoosimm_alternative = mancoosimm_alternative;
    }
    public mancoosimm_SkeeperCatalog getMancoosimm_skeepercatalog() {
        return mancoosimm_skeepercatalog;
    }

    public void setMancoosimm_skeepercatalog(mancoosimm_SkeeperCatalog mancoosimm_skeepercatalog) {
        this.mancoosimm_skeepercatalog = mancoosimm_skeepercatalog;
    }
    public List<mancoosimm_Alternative> getMancoosimm_alternatives() {
        return mancoosimm_alternatives;
    }

    public void addMancoosimm_alternative(Mancoosimm_alternative mancoosimm_alternative) {
        this.mancoosimm_alternatives.add(mancoosimm_alternative);
    }
    public mancoosimm_Configuration getMancoosimm_configuration() {
        return mancoosimm_configuration;
    }

    public void setMancoosimm_configuration(mancoosimm_Configuration mancoosimm_configuration) {
        this.mancoosimm_configuration = mancoosimm_configuration;
    }
    public mancoosimm_SkeeperCatalog getMancoosimm_skeepercatalog() {
        return mancoosimm_skeepercatalog;
    }

    public void setMancoosimm_skeepercatalog(mancoosimm_SkeeperCatalog mancoosimm_skeepercatalog) {
        this.mancoosimm_skeepercatalog = mancoosimm_skeepercatalog;
    }
    public mancoosimm_Configuration getMancoosimm_configuration() {
        return mancoosimm_configuration;
    }

    public void setMancoosimm_configuration(mancoosimm_Configuration mancoosimm_configuration) {
        this.mancoosimm_configuration = mancoosimm_configuration;
    }

}