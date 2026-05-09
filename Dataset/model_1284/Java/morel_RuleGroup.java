





import java.util.List;
import java.util.ArrayList;

public class morel_RuleGroup extends RuleElement {

    private int maxIteration;
    private String iteration;
    private int scopeSize;
    private String order;
    private String scope;
    private String repetition;





    private List<morel_Rule> morel_rules;


    public morel_RuleGroup(
        int maxIteration,        String iteration,        int scopeSize,        String order,        String scope,        String repetition    ) {
        super(
        );
        this.maxIteration = maxIteration;
        this.iteration = iteration;
        this.scopeSize = scopeSize;
        this.order = order;
        this.scope = scope;
        this.repetition = repetition;
        this.morel_rules = new ArrayList<>();
    }

    public morel_RuleGroup(
        int maxIteration,        String iteration,        int scopeSize,        String order,        String scope,        String repetition        ArrayList<morel_Rule> morel_rules    ) {
        this.maxIteration = maxIteration;
        this.iteration = iteration;
        this.scopeSize = scopeSize;
        this.order = order;
        this.scope = scope;
        this.repetition = repetition;
        this.morel_rules = morel_rules;
    }

    public int getMaxiteration() {
        return maxIteration;
    }

    public void setMaxiteration(int maxIteration) {
        this.maxIteration = maxIteration;
    }
    public String getIteration() {
        return iteration;
    }

    public void setIteration(String iteration) {
        this.iteration = iteration;
    }
    public int getScopesize() {
        return scopeSize;
    }

    public void setScopesize(int scopeSize) {
        this.scopeSize = scopeSize;
    }
    public String getOrder() {
        return order;
    }

    public void setOrder(String order) {
        this.order = order;
    }
    public String getScope() {
        return scope;
    }

    public void setScope(String scope) {
        this.scope = scope;
    }
    public String getRepetition() {
        return repetition;
    }

    public void setRepetition(String repetition) {
        this.repetition = repetition;
    }

    public List<morel_Rule> getMorel_rules() {
        return morel_rules;
    }

    public void addMorel_rule(Morel_rule morel_rule) {
        this.morel_rules.add(morel_rule);
    }

}