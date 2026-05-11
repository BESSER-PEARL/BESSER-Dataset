





import java.util.List;
import java.util.ArrayList;

public class selflet_SelfletProperties  {

    private String enableCloudOptimizationPolicy;
    private String author;
    private String limePort;
    private String description;
    private String enableOptimizationPolicy;





    private selflet_Selflet selflet_selflet;


    public selflet_SelfletProperties(
        String enableCloudOptimizationPolicy,        String author,        String limePort,        String description,        String enableOptimizationPolicy    ) {
        this.enableCloudOptimizationPolicy = enableCloudOptimizationPolicy;
        this.author = author;
        this.limePort = limePort;
        this.description = description;
        this.enableOptimizationPolicy = enableOptimizationPolicy;
    }


    public String getEnablecloudoptimizationpolicy() {
        return enableCloudOptimizationPolicy;
    }

    public void setEnablecloudoptimizationpolicy(String enableCloudOptimizationPolicy) {
        this.enableCloudOptimizationPolicy = enableCloudOptimizationPolicy;
    }
    public String getAuthor() {
        return author;
    }

    public void setAuthor(String author) {
        this.author = author;
    }
    public String getLimeport() {
        return limePort;
    }

    public void setLimeport(String limePort) {
        this.limePort = limePort;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getEnableoptimizationpolicy() {
        return enableOptimizationPolicy;
    }

    public void setEnableoptimizationpolicy(String enableOptimizationPolicy) {
        this.enableOptimizationPolicy = enableOptimizationPolicy;
    }

    public selflet_Selflet getSelflet_selflet() {
        return selflet_selflet;
    }

    public void setSelflet_selflet(selflet_Selflet selflet_selflet) {
        this.selflet_selflet = selflet_selflet;
    }

}