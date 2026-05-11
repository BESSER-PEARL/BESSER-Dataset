





import java.util.List;
import java.util.ArrayList;

public class p2_Requirement extends ModelElement {

    private boolean optional;
    private String filter;
    private String name;
    private String versionRange;
    private String namespace;
    private String type;
    private String iD;





    private p2_ProfileDefinition p2_profiledefinition;


    public p2_Requirement(
        boolean optional,        String filter,        String name,        String versionRange,        String namespace,        String type,        String iD    ) {
        super(
        );
        this.optional = optional;
        this.filter = filter;
        this.name = name;
        this.versionRange = versionRange;
        this.namespace = namespace;
        this.type = type;
        this.iD = iD;
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
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getVersionrange() {
        return versionRange;
    }

    public void setVersionrange(String versionRange) {
        this.versionRange = versionRange;
    }
    public String getNamespace() {
        return namespace;
    }

    public void setNamespace(String namespace) {
        this.namespace = namespace;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getId() {
        return iD;
    }

    public void setId(String iD) {
        this.iD = iD;
    }

    public p2_ProfileDefinition getP2_profiledefinition() {
        return p2_profiledefinition;
    }

    public void setP2_profiledefinition(p2_ProfileDefinition p2_profiledefinition) {
        this.p2_profiledefinition = p2_profiledefinition;
    }

}