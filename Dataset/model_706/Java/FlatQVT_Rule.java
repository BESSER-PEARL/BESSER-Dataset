





import java.util.List;
import java.util.ArrayList;

public class FlatQVT_Rule extends NamedElement {






    private List<Domain> domains;


    public FlatQVT_Rule(
    ) {
        super(
        );
        this.domains = new ArrayList<>();
    }

    public FlatQVT_Rule(
        ArrayList<Domain> domains    ) {
        this.domains = domains;
    }


    public List<Domain> getDomains() {
        return domains;
    }

    public void addDomain(Domain domain) {
        this.domains.add(domain);
    }

}