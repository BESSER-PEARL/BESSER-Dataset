





import java.util.List;
import java.util.ArrayList;

public class p2_Requirement extends ModelElement {

    private String type;
    private String versionRange;
    private boolean greedy;
    private boolean optional;
    private String filter;
    private String namespace;
    private String name;
    private String iD;



    public p2_Requirement(
        String type,        String versionRange,        boolean greedy,        boolean optional,        String filter,        String namespace,        String name,        String iD    ) {
        super(
        );
        this.type = type;
        this.versionRange = versionRange;
        this.greedy = greedy;
        this.optional = optional;
        this.filter = filter;
        this.namespace = namespace;
        this.name = name;
        this.iD = iD;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getVersionrange() {
        return versionRange;
    }

    public void setVersionrange(String versionRange) {
        this.versionRange = versionRange;
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
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getId() {
        return iD;
    }

    public void setId(String iD) {
        this.iD = iD;
    }


}