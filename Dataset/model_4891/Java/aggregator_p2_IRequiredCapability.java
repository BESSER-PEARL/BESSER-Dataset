





import java.util.List;
import java.util.ArrayList;

public class aggregator_p2_IRequiredCapability  {

    private String namespace;
    private boolean optional;
    private String range;
    private boolean negation;
    private String filter;
    private String selectorList;
    private String name;
    private boolean greedy;
    private boolean multiple;



    public aggregator_p2_IRequiredCapability(
        String namespace,        boolean optional,        String range,        boolean negation,        String filter,        String selectorList,        String name,        boolean greedy,        boolean multiple    ) {
        this.namespace = namespace;
        this.optional = optional;
        this.range = range;
        this.negation = negation;
        this.filter = filter;
        this.selectorList = selectorList;
        this.name = name;
        this.greedy = greedy;
        this.multiple = multiple;
    }


    public String getNamespace() {
        return namespace;
    }

    public void setNamespace(String namespace) {
        this.namespace = namespace;
    }
    public boolean getOptional() {
        return optional;
    }

    public void setOptional(boolean optional) {
        this.optional = optional;
    }
    public String getRange() {
        return range;
    }

    public void setRange(String range) {
        this.range = range;
    }
    public boolean getNegation() {
        return negation;
    }

    public void setNegation(boolean negation) {
        this.negation = negation;
    }
    public String getFilter() {
        return filter;
    }

    public void setFilter(String filter) {
        this.filter = filter;
    }
    public String getSelectorlist() {
        return selectorList;
    }

    public void setSelectorlist(String selectorList) {
        this.selectorList = selectorList;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getGreedy() {
        return greedy;
    }

    public void setGreedy(boolean greedy) {
        this.greedy = greedy;
    }
    public boolean getMultiple() {
        return multiple;
    }

    public void setMultiple(boolean multiple) {
        this.multiple = multiple;
    }


}