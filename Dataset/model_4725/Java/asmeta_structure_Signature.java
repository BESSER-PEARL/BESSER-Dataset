





import java.util.List;
import java.util.ArrayList;

public class asmeta_structure_Signature  {






    private List<Function> functions;




    private List<domains_Domain> domains_domains;


    public asmeta_structure_Signature(
    ) {
        this.functions = new ArrayList<>();
        this.domains_domains = new ArrayList<>();
    }

    public asmeta_structure_Signature(
        ArrayList<Function> functions,        ArrayList<domains_Domain> domains_domains    ) {
        this.functions = functions;
        this.domains_domains = domains_domains;
    }


    public List<Function> getFunctions() {
        return functions;
    }

    public void addFunction(Function function) {
        this.functions.add(function);
    }
    public List<domains_Domain> getDomains_domains() {
        return domains_domains;
    }

    public void addDomains_domain(Domains_domain domains_domain) {
        this.domains_domains.add(domains_domain);
    }

}