





import java.util.List;
import java.util.ArrayList;

public class aggregator_p2_IRequiredCapability  {

    private boolean greedy;
    private boolean optional;
    private boolean multiple;
    private String range;
    private String selectorList;
    private String filter;
    private String name;
    private String namespace;
    private boolean negation;



    public aggregator_p2_IRequiredCapability(
        boolean greedy,        boolean optional,        boolean multiple,        String range,        String selectorList,        String filter,        String name,        String namespace,        boolean negation    ) {
        this.greedy = greedy;
        this.optional = optional;
        this.multiple = multiple;
        this.range = range;
        this.selectorList = selectorList;
        this.filter = filter;
        this.name = name;
        this.namespace = namespace;
        this.negation = negation;
    }


    public boolean getGreedy() {
        return greedy;
    }

    public void setGreedy(boolean greedy) {
        this.greedy = greedy;
    }
    public boolean getOptional() {
        return optional;
    }

    public void setOptional(boolean optional) {
        this.optional = optional;
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
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getNamespace() {
        return namespace;
    }

    public void setNamespace(String namespace) {
        this.namespace = namespace;
    }
    public boolean getNegation() {
        return negation;
    }

    public void setNegation(boolean negation) {
        this.negation = negation;
    }


}