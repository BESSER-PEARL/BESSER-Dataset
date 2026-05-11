





import java.util.List;
import java.util.ArrayList;

public class aggregator_p2view_IUPresentation  {

    private String label;
    private String name;
    private String id;
    private String version;
    private String description;
    private String type;





    private InstallableUnit installableunit;


    public aggregator_p2view_IUPresentation(
        String label,        String name,        String id,        String version,        String description,        String type    ) {
        this.label = label;
        this.name = name;
        this.id = id;
        this.version = version;
        this.description = description;
        this.type = type;
    }


    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public InstallableUnit getInstallableunit() {
        return installableunit;
    }

    public void setInstallableunit(InstallableUnit installableunit) {
        this.installableunit = installableunit;
    }

}