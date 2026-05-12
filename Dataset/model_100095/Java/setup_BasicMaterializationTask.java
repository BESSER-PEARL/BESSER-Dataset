





import java.util.List;
import java.util.ArrayList;

public class setup_BasicMaterializationTask extends SetupTask {

    private String bundlePool;
    private String targetPlatform;



    public setup_BasicMaterializationTask(
        String bundlePool,        String targetPlatform    ) {
        super(
        );
        this.bundlePool = bundlePool;
        this.targetPlatform = targetPlatform;
    }


    public String getBundlepool() {
        return bundlePool;
    }

    public void setBundlepool(String bundlePool) {
        this.bundlePool = bundlePool;
    }
    public String getTargetplatform() {
        return targetPlatform;
    }

    public void setTargetplatform(String targetPlatform) {
        this.targetPlatform = targetPlatform;
    }


}