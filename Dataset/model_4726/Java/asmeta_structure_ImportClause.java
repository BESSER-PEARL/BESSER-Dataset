





import java.util.List;
import java.util.ArrayList;

public class asmeta_structure_ImportClause  {

    private String moduleName;





    private List<RuleDeclaration> ruledeclarations;




    private List<domains_Domain> domains_domains;




    private List<Function> functions;


    public asmeta_structure_ImportClause(
        String moduleName    ) {
        this.moduleName = moduleName;
        this.ruledeclarations = new ArrayList<>();
        this.domains_domains = new ArrayList<>();
        this.functions = new ArrayList<>();
    }

    public asmeta_structure_ImportClause(
        String moduleName        ArrayList<RuleDeclaration> ruledeclarations,        ArrayList<domains_Domain> domains_domains,        ArrayList<Function> functions    ) {
        this.moduleName = moduleName;
        this.ruledeclarations = ruledeclarations;
        this.domains_domains = domains_domains;
        this.functions = functions;
    }

    public String getModulename() {
        return moduleName;
    }

    public void setModulename(String moduleName) {
        this.moduleName = moduleName;
    }

    public List<RuleDeclaration> getRuledeclarations() {
        return ruledeclarations;
    }

    public void addRuledeclaration(Ruledeclaration ruledeclaration) {
        this.ruledeclarations.add(ruledeclaration);
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