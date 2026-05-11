





import java.util.List;
import java.util.ArrayList;

public class cloudml_core_ResourcesPool extends CloudMLElementWithProperties {

    private String type;
    private int minReplicats;
    private int nbReplicats;
    private int maxReplicats;



    public cloudml_core_ResourcesPool(
        String type,        int minReplicats,        int nbReplicats,        int maxReplicats    ) {
        super(
        );
        this.type = type;
        this.minReplicats = minReplicats;
        this.nbReplicats = nbReplicats;
        this.maxReplicats = maxReplicats;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
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
    public int getMaxreplicats() {
        return maxReplicats;
    }

    public void setMaxreplicats(int maxReplicats) {
        this.maxReplicats = maxReplicats;
    }


}