





import java.util.List;
import java.util.ArrayList;

public class Cluster  {

    private String populate;





    private Redis redis;


    public Cluster(
        String populate    ) {
        this.populate = populate;
    }


    public String getPopulate() {
        return populate;
    }

    public void setPopulate(String populate) {
        this.populate = populate;
    }

    public Redis getRedis() {
        return redis;
    }

    public void setRedis(Redis redis) {
        this.redis = redis;
    }

}