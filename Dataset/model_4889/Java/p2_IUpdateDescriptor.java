





import java.util.List;
import java.util.ArrayList;

public class p2_IUpdateDescriptor  {

    private String description;
    private int severity;
    private String location;





    private p2_IInstallableUnit p2_iinstallableunit;


    public p2_IUpdateDescriptor(
        String description,        int severity,        String location    ) {
        this.description = description;
        this.severity = severity;
        this.location = location;
    }


    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public int getSeverity() {
        return severity;
    }

    public void setSeverity(int severity) {
        this.severity = severity;
    }
    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
        this.location = location;
    }

    public p2_IInstallableUnit getP2_iinstallableunit() {
        return p2_iinstallableunit;
    }

    public void setP2_iinstallableunit(p2_IInstallableUnit p2_iinstallableunit) {
        this.p2_iinstallableunit = p2_iinstallableunit;
    }

}