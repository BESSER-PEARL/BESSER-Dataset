





import java.util.List;
import java.util.ArrayList;

public class aggregator_p2_IRequiredCapability  {

    private String name;
    private boolean optional;
    private String filter;
    private String selectorList;
    private boolean multiple;
    private String range;
    private String namespace;
    private boolean greedy;
    private boolean negation;



    public aggregator_p2_IRequiredCapability(
        String name,        boolean optional,        String filter,        String selectorList,        boolean multiple,        String range,        String namespace,        boolean greedy,        boolean negation    ) {
        this.name = name;
        this.optional = optional;
        this.filter = filter;
        this.selectorList = selectorList;
        this.multiple = multiple;
        this.range = range;
        this.namespace = namespace;
        this.greedy = greedy;
        this.negation = negation;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
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
    public String getSelectorlist() {
        return selectorList;
    }

    public void setSelectorlist(String selectorList) {
        this.selectorList = selectorList;
    }
    public boolean getMultiple() {
        return multiple;
    }

    public void setMultiple(boolean multiple) {
        this.multiple = multiple;
    }
    public String getRange() {
        return range;
    }

    public void setRange(String range) {
        this.range = range;
    }
    public String getNamespace() {
        return namespace;
    }

    public void setNamespace(String namespace) {
        this.namespace = namespace;
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


}