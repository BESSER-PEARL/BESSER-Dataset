





import java.util.List;
import java.util.ArrayList;

public class uml_BehavioralFeature extends Namespace, Feature {

    private String isAbstract;
    private String concurrency;



    public uml_BehavioralFeature(
        String isAbstract,        String concurrency    ) {
        super(
        );
        this.isAbstract = isAbstract;
        this.concurrency = concurrency;
    }


    public String getIsabstract() {
        return isAbstract;
    }

    public void setIsabstract(String isAbstract) {
        this.isAbstract = isAbstract;
    }
    public String getConcurrency() {
        return concurrency;
    }

    public void setConcurrency(String concurrency) {
        this.concurrency = concurrency;
    }


}