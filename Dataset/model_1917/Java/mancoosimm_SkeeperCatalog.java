





import java.util.List;
import java.util.ArrayList;

public class mancoosimm_SkeeperCatalog extends NamedElement {






    private mancoosimm_Environment mancoosimm_environment;




    private mancoosimm_Environment mancoosimm_environment;




    private List<mancoosimm_SkeeperDocument> mancoosimm_skeeperdocuments;


    public mancoosimm_SkeeperCatalog(
    ) {
        super(
        );
        this.mancoosimm_skeeperdocuments = new ArrayList<>();
    }

    public mancoosimm_SkeeperCatalog(
        ArrayList<mancoosimm_SkeeperDocument> mancoosimm_skeeperdocuments    ) {
        this.mancoosimm_skeeperdocuments = mancoosimm_skeeperdocuments;
    }


    public mancoosimm_Environment getMancoosimm_environment() {
        return mancoosimm_environment;
    }

    public void setMancoosimm_environment(mancoosimm_Environment mancoosimm_environment) {
        this.mancoosimm_environment = mancoosimm_environment;
    }
    public mancoosimm_Environment getMancoosimm_environment() {
        return mancoosimm_environment;
    }

    public void setMancoosimm_environment(mancoosimm_Environment mancoosimm_environment) {
        this.mancoosimm_environment = mancoosimm_environment;
    }
    public List<mancoosimm_SkeeperDocument> getMancoosimm_skeeperdocuments() {
        return mancoosimm_skeeperdocuments;
    }

    public void addMancoosimm_skeeperdocument(Mancoosimm_skeeperdocument mancoosimm_skeeperdocument) {
        this.mancoosimm_skeeperdocuments.add(mancoosimm_skeeperdocument);
    }

}