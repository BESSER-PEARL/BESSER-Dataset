





import java.util.List;
import java.util.ArrayList;

public class model_StringToHost  {

    private String key;





    private model_Cluster model_cluster;


    public model_StringToHost(
        String key    ) {
        this.key = key;
    }


    public String getKey() {
        return key;
    }

    public void setKey(String key) {
        this.key = key;
    }

    public model_Cluster getModel_cluster() {
        return model_cluster;
    }

    public void setModel_cluster(model_Cluster model_cluster) {
        this.model_cluster = model_cluster;
    }

}