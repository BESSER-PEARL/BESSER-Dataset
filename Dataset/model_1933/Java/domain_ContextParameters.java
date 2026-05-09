





import java.util.List;
import java.util.ArrayList;

public class domain_ContextParameters  {






    private List<domain_ContextParameter> domain_contextparameters;


    public domain_ContextParameters(
    ) {
        this.domain_contextparameters = new ArrayList<>();
    }

    public domain_ContextParameters(
        ArrayList<domain_ContextParameter> domain_contextparameters    ) {
        this.domain_contextparameters = domain_contextparameters;
    }


    public List<domain_ContextParameter> getDomain_contextparameters() {
        return domain_contextparameters;
    }

    public void addDomain_contextparameter(Domain_contextparameter domain_contextparameter) {
        this.domain_contextparameters.add(domain_contextparameter);
    }

}