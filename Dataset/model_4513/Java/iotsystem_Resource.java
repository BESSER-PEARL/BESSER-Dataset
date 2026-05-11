





import java.util.List;
import java.util.ArrayList;

public class iotsystem_Resource  {

    private String measurement;
    private String url;





    private iotsystem_DigitalArtifact iotsystem_digitalartifact;




    private iotsystem_Device iotsystem_device;


    public iotsystem_Resource(
        String measurement,        String url    ) {
        this.measurement = measurement;
        this.url = url;
    }


    public String getMeasurement() {
        return measurement;
    }

    public void setMeasurement(String measurement) {
        this.measurement = measurement;
    }
    public String getUrl() {
        return url;
    }

    public void setUrl(String url) {
        this.url = url;
    }

    public iotsystem_DigitalArtifact getIotsystem_digitalartifact() {
        return iotsystem_digitalartifact;
    }

    public void setIotsystem_digitalartifact(iotsystem_DigitalArtifact iotsystem_digitalartifact) {
        this.iotsystem_digitalartifact = iotsystem_digitalartifact;
    }
    public iotsystem_Device getIotsystem_device() {
        return iotsystem_device;
    }

    public void setIotsystem_device(iotsystem_Device iotsystem_device) {
        this.iotsystem_device = iotsystem_device;
    }

}