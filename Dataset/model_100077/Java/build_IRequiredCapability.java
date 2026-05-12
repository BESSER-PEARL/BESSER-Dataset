





import java.util.List;
import java.util.ArrayList;

public class build_IRequiredCapability  {

    private String range;
    private String name;
    private String filter;
    private String namespace;



    public build_IRequiredCapability(
        String range,        String name,        String filter,        String namespace    ) {
        this.range = range;
        this.name = name;
        this.filter = filter;
        this.namespace = namespace;
    }


    public String getRange() {
        return range;
    }

    public void setRange(String range) {
        this.range = range;
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
    public String getNamespace() {
        return namespace;
    }

    public void setNamespace(String namespace) {
        this.namespace = namespace;
    }


}