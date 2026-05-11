





import java.util.List;
import java.util.ArrayList;

public class aggregator_p2_IRequiredCapability  {

    private String namespace;
    private boolean optional;
    private boolean greedy;
    private boolean multiple;
    private boolean negation;
    private String name;
    private String filter;
    private String range;
    private String selectorList;



    public aggregator_p2_IRequiredCapability(
        String namespace,        boolean optional,        boolean greedy,        boolean multiple,        boolean negation,        String name,        String filter,        String range,        String selectorList    ) {
        this.namespace = namespace;
        this.optional = optional;
        this.greedy = greedy;
        this.multiple = multiple;
        this.negation = negation;
        this.name = name;
        this.filter = filter;
        this.range = range;
        this.selectorList = selectorList;
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
    public boolean getNegation() {
        return negation;
    }

    public void setNegation(boolean negation) {
        this.negation = negation;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getFilter() {
        return filter;
    }

    public void setFilter(String filter) {
        this.filter = filter;
    }
    public String getRange() {
        return range;
    }

    public void setRange(String range) {
        this.range = range;
    }
    public String getSelectorlist() {
        return selectorList;
    }

    public void setSelectorlist(String selectorList) {
        this.selectorList = selectorList;
    }


}