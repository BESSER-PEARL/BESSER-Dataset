





import java.util.List;
import java.util.ArrayList;

public class di_BPMNDiagram extends Diagram {

    private String location;
    private String featureModel;
    private String phase;
    private String version;





    private di_DocumentRoot di_documentroot;


    public di_BPMNDiagram(
        String location,        String featureModel,        String phase,        String version    ) {
        super(
        );
        this.location = location;
        this.featureModel = featureModel;
        this.phase = phase;
        this.version = version;
    }


    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
        this.location = location;
    }
    public String getFeaturemodel() {
        return featureModel;
    }

    public void setFeaturemodel(String featureModel) {
        this.featureModel = featureModel;
    }
    public String getPhase() {
        return phase;
    }

    public void setPhase(String phase) {
        this.phase = phase;
    }
    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }

    public di_DocumentRoot getDi_documentroot() {
        return di_documentroot;
    }

    public void setDi_documentroot(di_DocumentRoot di_documentroot) {
        this.di_documentroot = di_documentroot;
    }

}