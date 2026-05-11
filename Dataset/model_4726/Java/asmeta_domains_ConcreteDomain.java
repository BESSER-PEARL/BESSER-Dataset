





import java.util.List;
import java.util.ArrayList;

public class asmeta_domains_ConcreteDomain extends Domain {

    private String isDynamic;





    private List<DomainInitialization> domaininitializations;




    private DomainDefinition domaindefinition;


    public asmeta_domains_ConcreteDomain(
        String isDynamic    ) {
        super(
        );
        this.isDynamic = isDynamic;
        this.domaininitializations = new ArrayList<>();
    }

    public asmeta_domains_ConcreteDomain(
        String isDynamic        ArrayList<DomainInitialization> domaininitializations    ) {
        this.isDynamic = isDynamic;
        this.domaininitializations = domaininitializations;
    }

    public String getIsdynamic() {
        return isDynamic;
    }

    public void setIsdynamic(String isDynamic) {
        this.isDynamic = isDynamic;
    }

    public List<DomainInitialization> getDomaininitializations() {
        return domaininitializations;
    }

    public void addDomaininitialization(Domaininitialization domaininitialization) {
        this.domaininitializations.add(domaininitialization);
    }
    public DomainDefinition getDomaindefinition() {
        return domaindefinition;
    }

    public void setDomaindefinition(DomainDefinition domaindefinition) {
        this.domaindefinition = domaindefinition;
    }

}