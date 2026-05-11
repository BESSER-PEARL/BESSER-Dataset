





import java.util.List;
import java.util.ArrayList;

public class smif_toplevel_IdentifiableEntity extends Thing {






    private List<Identifier> identifiers;




    private Identifier identifier;




    private List<Rule> rules;


    public smif_toplevel_IdentifiableEntity(
    ) {
        super(
        );
        this.identifiers = new ArrayList<>();
        this.rules = new ArrayList<>();
    }

    public smif_toplevel_IdentifiableEntity(
        ArrayList<Identifier> identifiers,        ArrayList<Rule> rules    ) {
        this.identifiers = identifiers;
        this.rules = rules;
    }


    public List<Identifier> getIdentifiers() {
        return identifiers;
    }

    public void addIdentifier(Identifier identifier) {
        this.identifiers.add(identifier);
    }
    public Identifier getIdentifier() {
        return identifier;
    }

    public void setIdentifier(Identifier identifier) {
        this.identifier = identifier;
    }
    public List<Rule> getRules() {
        return rules;
    }

    public void addRule(Rule rule) {
        this.rules.add(rule);
    }

}