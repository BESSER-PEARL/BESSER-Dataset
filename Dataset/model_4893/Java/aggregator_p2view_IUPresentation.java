





import java.util.List;
import java.util.ArrayList;

public class aggregator_p2view_IUPresentation  {

    private String description;
    private String type;
    private String version;
    private String name;
    private String id;
    private String label;





    private InstallableUnit installableunit;


    public aggregator_p2view_IUPresentation(
        String description,        String type,        String version,        String name,        String id,        String label    ) {
        this.description = description;
        this.type = type;
        this.version = version;
        this.name = name;
        this.id = id;
        this.label = label;
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
    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
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
    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }

    public InstallableUnit getInstallableunit() {
        return installableunit;
    }

    public void setInstallableunit(InstallableUnit installableunit) {
        this.installableunit = installableunit;
    }

}