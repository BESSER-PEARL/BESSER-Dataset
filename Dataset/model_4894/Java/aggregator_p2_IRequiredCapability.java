





import java.util.List;
import java.util.ArrayList;

public class aggregator_p2_IRequiredCapability  {

    private boolean optional;
    private String filter;
    private String range;
    private boolean multiple;
    private String selectorList;
    private boolean greedy;
    private boolean negation;
    private String namespace;
    private String name;



    public aggregator_p2_IRequiredCapability(
        boolean optional,        String filter,        String range,        boolean multiple,        String selectorList,        boolean greedy,        boolean negation,        String namespace,        String name    ) {
        this.optional = optional;
        this.filter = filter;
        this.range = range;
        this.multiple = multiple;
        this.selectorList = selectorList;
        this.greedy = greedy;
        this.negation = negation;
        this.namespace = namespace;
        this.name = name;
    }


    public boolean getOptional() {
        return optional;
    }

    public void setOptional(boolean optional) {
        this.optional = optional;
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
    public boolean getGreedy() {
        return greedy;
    }

    public void setGreedy(boolean greedy) {
        this.greedy = greedy;
    }
    public boolean getNegation() {
        return negation;
    }

    public void setNegation(boolean negation) {
        this.negation = negation;
    }
    public String getNamespace() {
        return namespace;
    }

    public void setNamespace(String namespace) {
        this.namespace = namespace;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}