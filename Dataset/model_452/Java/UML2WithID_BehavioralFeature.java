





import java.util.List;
import java.util.ArrayList;

public class UML2WithID_BehavioralFeature extends Feature, Namespace {

    private String concurrency;
    private boolean isAbstract;



    public UML2WithID_BehavioralFeature(
        String concurrency,        boolean isAbstract    ) {
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
    public boolean getIsabstract() {
        return isAbstract;
    }

    public void setIsabstract(boolean isAbstract) {
        this.isAbstract = isAbstract;
    }


}