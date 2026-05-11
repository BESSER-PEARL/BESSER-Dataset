





import java.util.List;
import java.util.ArrayList;

public class aggregator_p2_IRequiredCapability  {

    private boolean optional;
    private String selectorList;
    private String filter;
    private boolean negation;
    private String name;
    private String range;
    private boolean multiple;
    private String namespace;
    private boolean greedy;



    public aggregator_p2_IRequiredCapability(
        boolean optional,        String selectorList,        String filter,        boolean negation,        String name,        String range,        boolean multiple,        String namespace,        boolean greedy    ) {
        this.optional = optional;
        this.selectorList = selectorList;
        this.filter = filter;
        this.negation = negation;
        this.name = name;
        this.range = range;
        this.multiple = multiple;
        this.namespace = namespace;
        this.greedy = greedy;
    }


    public boolean getOptional() {
        return optional;
    }

    public void setOptional(boolean optional) {
        this.optional = optional;
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


}