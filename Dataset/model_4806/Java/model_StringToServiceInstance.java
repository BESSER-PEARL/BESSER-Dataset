





import java.util.List;
import java.util.ArrayList;

public class model_StringToServiceInstance  {

    private String key;





    private model_Host model_host;


    public model_StringToServiceInstance(
        String key    ) {
        this.key = key;
    }


    public String getKey() {
        return key;
    }

    public void setKey(String key) {
        this.key = key;
    }

    public model_Host getModel_host() {
        return model_host;
    }

    public void setModel_host(model_Host model_host) {
        this.model_host = model_host;
    }

}