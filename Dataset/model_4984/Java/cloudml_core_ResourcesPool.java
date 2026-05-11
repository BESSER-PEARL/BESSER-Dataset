





import java.util.List;
import java.util.ArrayList;

public class cloudml_core_ResourcesPool extends CloudMLElementWithProperties {

    private int minReplicats;
    private int nbReplicats;
    private String type;
    private int maxReplicats;



    public cloudml_core_ResourcesPool(
        int minReplicats,        int nbReplicats,        String type,        int maxReplicats    ) {
        super(
        );
        this.minReplicats = minReplicats;
        this.nbReplicats = nbReplicats;
        this.type = type;
        this.maxReplicats = maxReplicats;
    }


    public int getMinreplicats() {
        return minReplicats;
    }

    public void setMinreplicats(int minReplicats) {
        this.minReplicats = minReplicats;
    }
    public int getNbreplicats() {
        return nbReplicats;
    }

    public void setNbreplicats(int nbReplicats) {
        this.nbReplicats = nbReplicats;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public int getMaxreplicats() {
        return maxReplicats;
    }

    public void setMaxreplicats(int maxReplicats) {
        this.maxReplicats = maxReplicats;
    }


}