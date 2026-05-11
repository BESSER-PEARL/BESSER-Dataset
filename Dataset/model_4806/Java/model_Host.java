





import java.util.List;
import java.util.ArrayList;

public class model_Host extends ElementWithResources {

    private String name;
    private String hostAddress;
    private String cores;





    private model_StringToHost model_stringtohost;


    public model_Host(
        String name,        String hostAddress,        String cores    ) {
        super(
        );
        this.name = name;
        this.hostAddress = hostAddress;
        this.cores = cores;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getHostaddress() {
        return hostAddress;
    }

    public void setHostaddress(String hostAddress) {
        this.hostAddress = hostAddress;
    }
    public String getCores() {
        return cores;
    }

    public void setCores(String cores) {
        this.cores = cores;
    }

    public model_StringToHost getModel_stringtohost() {
        return model_stringtohost;
    }

    public void setModel_stringtohost(model_StringToHost model_stringtohost) {
        this.model_stringtohost = model_stringtohost;
    }

}