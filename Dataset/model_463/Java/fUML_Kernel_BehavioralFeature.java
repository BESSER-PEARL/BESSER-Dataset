





import java.util.List;
import java.util.ArrayList;

public class fUML_Kernel_BehavioralFeature extends Feature {

    private String concurrency;
    private boolean abstract;



    public fUML_Kernel_BehavioralFeature(
        String concurrency,        boolean abstract    ) {
        super(
        );
        this.concurrency = concurrency;
        this.abstract = abstract;
    }


    public String getConcurrency() {
        return concurrency;
    }

    public void setConcurrency(String concurrency) {
        this.concurrency = concurrency;
    }
    public boolean getAbstract() {
        return abstract;
    }

    public void setAbstract(boolean abstract) {
        this.abstract = abstract;
    }


}