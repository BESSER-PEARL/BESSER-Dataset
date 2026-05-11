





import java.util.List;
import java.util.ArrayList;

public class servicefeaturemodel_OR extends Variant {

    private int minFeaturesToChoose;
    private int maxFeaturesToChoose;



    public servicefeaturemodel_OR(
        int minFeaturesToChoose,        int maxFeaturesToChoose    ) {
        super(
        );
        this.minFeaturesToChoose = minFeaturesToChoose;
        this.maxFeaturesToChoose = maxFeaturesToChoose;
    }


    public int getMinfeaturestochoose() {
        return minFeaturesToChoose;
    }

    public void setMinfeaturestochoose(int minFeaturesToChoose) {
        this.minFeaturesToChoose = minFeaturesToChoose;
    }
    public int getMaxfeaturestochoose() {
        return maxFeaturesToChoose;
    }

    public void setMaxfeaturestochoose(int maxFeaturesToChoose) {
        this.maxFeaturesToChoose = maxFeaturesToChoose;
    }


}