





import java.util.List;
import java.util.ArrayList;

public class metrics_MetricSource  {

    private String metrickind;
    private String mappingFile;
    private String metricLocation;
    private String name;
    private String lastContact;
    private String lastPurge;



    public metrics_MetricSource(
        String metrickind,        String mappingFile,        String metricLocation,        String name,        String lastContact,        String lastPurge    ) {
        this.metrickind = metrickind;
        this.mappingFile = mappingFile;
        this.metricLocation = metricLocation;
        this.name = name;
        this.lastContact = lastContact;
        this.lastPurge = lastPurge;
    }


    public String getMetrickind() {
        return metrickind;
    }

    public void setMetrickind(String metrickind) {
        this.metrickind = metrickind;
    }
    public String getMappingfile() {
        return mappingFile;
    }

    public void setMappingfile(String mappingFile) {
        this.mappingFile = mappingFile;
    }
    public String getMetriclocation() {
        return metricLocation;
    }

    public void setMetriclocation(String metricLocation) {
        this.metricLocation = metricLocation;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getLastcontact() {
        return lastContact;
    }

    public void setLastcontact(String lastContact) {
        this.lastContact = lastContact;
    }
    public String getLastpurge() {
        return lastPurge;
    }

    public void setLastpurge(String lastPurge) {
        this.lastPurge = lastPurge;
    }


}