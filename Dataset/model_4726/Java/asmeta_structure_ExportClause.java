





import java.util.List;
import java.util.ArrayList;

public class asmeta_structure_ExportClause  {






    private List<domains_Domain> domains_domains;




    private List<RuleDeclaration> ruledeclarations;




    private List<Function> functions;


    public asmeta_structure_ExportClause(
    ) {
        this.domains_domains = new ArrayList<>();
        this.ruledeclarations = new ArrayList<>();
        this.functions = new ArrayList<>();
    }

    public asmeta_structure_ExportClause(
        ArrayList<domains_Domain> domains_domains,        ArrayList<RuleDeclaration> ruledeclarations,        ArrayList<Function> functions    ) {
        this.domains_domains = domains_domains;
        this.ruledeclarations = ruledeclarations;
        this.functions = functions;
    }


    public List<domains_Domain> getDomains_domains() {
        return domains_domains;
    }

    public void addDomains_domain(Domains_domain domains_domain) {
        this.domains_domains.add(domains_domain);
    }
    public List<RuleDeclaration> getRuledeclarations() {
        return ruledeclarations;
    }

    public void addRuledeclaration(Ruledeclaration ruledeclaration) {
        this.ruledeclarations.add(ruledeclaration);
    }
    public List<Function> getFunctions() {
        return functions;
    }

    public void addFunction(Function function) {
        this.functions.add(function);
    }

}