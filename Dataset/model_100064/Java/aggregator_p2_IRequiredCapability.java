





import java.util.List;
import java.util.ArrayList;

public class aggregator_p2_IRequiredCapability  {

    private String namespace;
    private boolean multiple;
    private String selectorList;
    private String filter;
    private boolean optional;
    private String name;
    private boolean negation;
    private boolean greedy;
    private String range;



    public aggregator_p2_IRequiredCapability(
        String namespace,        boolean multiple,        String selectorList,        String filter,        boolean optional,        String name,        boolean negation,        boolean greedy,        String range    ) {
        this.namespace = namespace;
        this.multiple = multiple;
        this.selectorList = selectorList;
        this.filter = filter;
        this.optional = optional;
        this.name = name;
        this.negation = negation;
        this.greedy = greedy;
        this.range = range;
    }


    public String getNamespace() {
        return namespace;
    }

    public void setNamespace(String namespace) {
        this.namespace = namespace;
    }
    public boolean getMultiple() {
        return multiple;
    }

    public void setMultiple(boolean multiple) {
        this.multiple = multiple;
    }
    public String getSelectorlist() {
        return selectorList;
    }

    public void setSelectorlist(String selectorList) {
        this.selectorList = selectorList;
    }
    public String getFilter() {
        return filter;
    }

    public void setFilter(String filter) {
        this.filter = filter;
    }
    public boolean getOptional() {
        return optional;
    }

    public void setOptional(boolean optional) {
        this.optional = optional;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getNegation() {
        return negation;
    }

    public void setNegation(boolean negation) {
        this.negation = negation;
    }
    public boolean getGreedy() {
        return greedy;
    }

    public void setGreedy(boolean greedy) {
        this.greedy = greedy;
    }
    public String getRange() {
        return range;
    }

    public void setRange(String range) {
        this.range = range;
    }


}