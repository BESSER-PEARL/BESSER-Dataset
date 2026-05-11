





import java.util.List;
import java.util.ArrayList;

public class pimm_FunctionPrototype extends PiMMVisitable {

    private String name;





    private List<pimm_FunctionParameter> pimm_functionparameters;


    public pimm_FunctionPrototype(
        String name    ) {
        super(
        );
        this.name = name;
        this.pimm_functionparameters = new ArrayList<>();
    }

    public pimm_FunctionPrototype(
        String name        ArrayList<pimm_FunctionParameter> pimm_functionparameters    ) {
        this.name = name;
        this.pimm_functionparameters = pimm_functionparameters;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<pimm_FunctionParameter> getPimm_functionparameters() {
        return pimm_functionparameters;
    }

    public void addPimm_functionparameter(Pimm_functionparameter pimm_functionparameter) {
        this.pimm_functionparameters.add(pimm_functionparameter);
    }

}