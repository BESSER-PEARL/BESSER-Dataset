





import java.util.List;
import java.util.ArrayList;

public class aggregator_p2view_IUPresentation  {

    private String type;
    private String name;
    private String description;
    private String version;
    private String label;
    private String id;





    private InstallableUnit installableunit;


    public aggregator_p2view_IUPresentation(
        String type,        String name,        String description,        String version,        String label,        String id    ) {
        this.type = type;
        this.name = name;
        this.description = description;
        this.version = version;
        this.label = label;
        this.id = id;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }
    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public InstallableUnit getInstallableunit() {
        return installableunit;
    }

    public void setInstallableunit(InstallableUnit installableunit) {
        this.installableunit = installableunit;
    }

}