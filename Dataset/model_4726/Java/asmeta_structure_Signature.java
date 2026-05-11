





import java.util.List;
import java.util.ArrayList;

public class asmeta_structure_Signature  {






    private List<domains_Domain> domains_domains;




    private List<Function> functions;


    public asmeta_structure_Signature(
    ) {
        this.domains_domains = new ArrayList<>();
        this.functions = new ArrayList<>();
    }

    public asmeta_structure_Signature(
        ArrayList<domains_Domain> domains_domains,        ArrayList<Function> functions    ) {
        this.domains_domains = domains_domains;
        this.functions = functions;
    }


    public List<domains_Domain> getDomains_domains() {
        return domains_domains;
    }

    public void addDomains_domain(Domains_domain domains_domain) {
        this.domains_domains.add(domains_domain);
    }
    public List<Function> getFunctions() {
        return functions;
    }

    public void addFunction(Function function) {
        this.functions.add(function);
    }

}