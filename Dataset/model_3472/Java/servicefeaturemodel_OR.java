





import java.util.List;
import java.util.ArrayList;

public class servicefeaturemodel_OR extends GroupRelationship {

    private int maxFeaturesToChoose;
    private int minFeaturesToChoose;



    public servicefeaturemodel_OR(
        int maxFeaturesToChoose,        int minFeaturesToChoose    ) {
        super(
        );
        this.maxFeaturesToChoose = maxFeaturesToChoose;
        this.minFeaturesToChoose = minFeaturesToChoose;
    }


    public int getMaxfeaturestochoose() {
        return maxFeaturesToChoose;
    }

    public void setMaxfeaturestochoose(int maxFeaturesToChoose) {
        this.maxFeaturesToChoose = maxFeaturesToChoose;
    }
    public int getMinfeaturestochoose() {
        return minFeaturesToChoose;
    }

    public void setMinfeaturestochoose(int minFeaturesToChoose) {
        this.minFeaturesToChoose = minFeaturesToChoose;
    }


}