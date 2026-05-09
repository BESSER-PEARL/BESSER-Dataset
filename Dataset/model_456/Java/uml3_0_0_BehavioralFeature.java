





import java.util.List;
import java.util.ArrayList;

public class uml3_0_0_BehavioralFeature extends Namespace, Feature {

    private String concurrency;
    private String isAbstract;



    public uml3_0_0_BehavioralFeature(
        String concurrency,        String isAbstract    ) {
        super(
        );
        this.concurrency = concurrency;
        this.isAbstract = isAbstract;
    }


    public String getConcurrency() {
        return concurrency;
    }

    public void setConcurrency(String concurrency) {
        this.concurrency = concurrency;
    }
    public String getIsabstract() {
        return isAbstract;
    }

    public void setIsabstract(String isAbstract) {
        this.isAbstract = isAbstract;
    }


}