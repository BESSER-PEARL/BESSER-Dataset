





import java.util.List;
import java.util.ArrayList;

public class test_SLAAssertion extends PerformanceAssertion {

    private String maxTime;



    public test_SLAAssertion(
        String maxTime    ) {
        super(
        );
        this.maxTime = maxTime;
    }


    public String getMaxtime() {
        return maxTime;
    }

    public void setMaxtime(String maxTime) {
        this.maxTime = maxTime;
    }


}