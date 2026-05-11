





import java.util.List;
import java.util.ArrayList;

public class asmeta_definitions_Invariant extends Property {






    private basicterms_Term basicterms_term;




    private List<RuleDeclaration> ruledeclarations;




    private List<Function> functions;




    private List<domains_Domain> domains_domains;


    public asmeta_definitions_Invariant(
    ) {
        super(
        );
        this.ruledeclarations = new ArrayList<>();
        this.functions = new ArrayList<>();
        this.domains_domains = new ArrayList<>();
    }

    public asmeta_definitions_Invariant(
        ArrayList<RuleDeclaration> ruledeclarations,        ArrayList<Function> functions,        ArrayList<domains_Domain> domains_domains    ) {
        this.ruledeclarations = ruledeclarations;
        this.functions = functions;
        this.domains_domains = domains_domains;
    }


    public basicterms_Term getBasicterms_term() {
        return basicterms_term;
    }

    public void setBasicterms_term(basicterms_Term basicterms_term) {
        this.basicterms_term = basicterms_term;
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
    public List<domains_Domain> getDomains_domains() {
        return domains_domains;
    }

    public void addDomains_domain(Domains_domain domains_domain) {
        this.domains_domains.add(domains_domain);
    }

}