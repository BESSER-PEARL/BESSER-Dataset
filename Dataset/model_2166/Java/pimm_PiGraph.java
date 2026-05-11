





import java.util.List;
import java.util.ArrayList;

public class pimm_PiGraph extends AbstractActor {






    private List<pimm_Parameter> pimm_parameters;




    private List<pimm_AbstractActor> pimm_abstractactors;


    public pimm_PiGraph(
    ) {
        super(
        );
        this.pimm_parameters = new ArrayList<>();
        this.pimm_abstractactors = new ArrayList<>();
    }

    public pimm_PiGraph(
        ArrayList<pimm_Parameter> pimm_parameters,        ArrayList<pimm_AbstractActor> pimm_abstractactors    ) {
        this.pimm_parameters = pimm_parameters;
        this.pimm_abstractactors = pimm_abstractactors;
    }


    public List<pimm_Parameter> getPimm_parameters() {
        return pimm_parameters;
    }

    public void addPimm_parameter(Pimm_parameter pimm_parameter) {
        this.pimm_parameters.add(pimm_parameter);
    }
    public List<pimm_AbstractActor> getPimm_abstractactors() {
        return pimm_abstractactors;
    }

    public void addPimm_abstractactor(Pimm_abstractactor pimm_abstractactor) {
        this.pimm_abstractactors.add(pimm_abstractactor);
    }

}