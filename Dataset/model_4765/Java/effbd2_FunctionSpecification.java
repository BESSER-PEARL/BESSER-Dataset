





import java.util.List;
import java.util.ArrayList;

public class effbd2_FunctionSpecification extends Transformer {

    private int minDuration;
    private String domain;
    private int maxDuration;



    public effbd2_FunctionSpecification(
        int minDuration,        String domain,        int maxDuration    ) {
        super(
        );
        this.minDuration = minDuration;
        this.domain = domain;
        this.maxDuration = maxDuration;
    }


    public int getMinduration() {
        return minDuration;
    }

    public void setMinduration(int minDuration) {
        this.minDuration = minDuration;
    }
    public String getDomain() {
        return domain;
    }

    public void setDomain(String domain) {
        this.domain = domain;
    }
    public int getMaxduration() {
        return maxDuration;
    }

    public void setMaxduration(int maxDuration) {
        this.maxDuration = maxDuration;
    }


}