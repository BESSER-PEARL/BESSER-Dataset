





import java.util.List;
import java.util.ArrayList;

public class selflet_SelfletProperties  {

    private String enableCloudOptimizationPolicy;
    private String limePort;
    private String description;
    private String author;
    private String enableOptimizationPolicy;





    private selflet_Reds selflet_reds;




    private selflet_Selflet selflet_selflet;




    private selflet_GeneralKnowledge selflet_generalknowledge;


    public selflet_SelfletProperties(
        String enableCloudOptimizationPolicy,        String limePort,        String description,        String author,        String enableOptimizationPolicy    ) {
        this.enableCloudOptimizationPolicy = enableCloudOptimizationPolicy;
        this.limePort = limePort;
        this.description = description;
        this.author = author;
        this.enableOptimizationPolicy = enableOptimizationPolicy;
    }


    public String getEnablecloudoptimizationpolicy() {
        return enableCloudOptimizationPolicy;
    }

    public void setEnablecloudoptimizationpolicy(String enableCloudOptimizationPolicy) {
        this.enableCloudOptimizationPolicy = enableCloudOptimizationPolicy;
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
    public String getAuthor() {
        return author;
    }

    public void setAuthor(String author) {
        this.author = author;
    }
    public String getEnableoptimizationpolicy() {
        return enableOptimizationPolicy;
    }

    public void setEnableoptimizationpolicy(String enableOptimizationPolicy) {
        this.enableOptimizationPolicy = enableOptimizationPolicy;
    }

    public selflet_Reds getSelflet_reds() {
        return selflet_reds;
    }

    public void setSelflet_reds(selflet_Reds selflet_reds) {
        this.selflet_reds = selflet_reds;
    }
    public selflet_Selflet getSelflet_selflet() {
        return selflet_selflet;
    }

    public void setSelflet_selflet(selflet_Selflet selflet_selflet) {
        this.selflet_selflet = selflet_selflet;
    }
    public selflet_GeneralKnowledge getSelflet_generalknowledge() {
        return selflet_generalknowledge;
    }

    public void setSelflet_generalknowledge(selflet_GeneralKnowledge selflet_generalknowledge) {
        this.selflet_generalknowledge = selflet_generalknowledge;
    }

}