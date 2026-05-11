





import java.util.List;
import java.util.ArrayList;

public class ftp_Component extends CompositionElement {

    private String type;
    private String name;





    private ftp_Observation ftp_observation;


    public ftp_Component(
        String type,        String name    ) {
        super(
        );
        this.type = type;
        this.name = name;
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

    public ftp_Observation getFtp_observation() {
        return ftp_observation;
    }

    public void setFtp_observation(ftp_Observation ftp_observation) {
        this.ftp_observation = ftp_observation;
    }

}