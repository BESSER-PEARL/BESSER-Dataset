





import java.util.List;
import java.util.ArrayList;

public class avm_modelica_Metric extends DomainModelMetric {

    private String Locator;



    public avm_modelica_Metric(
        String Locator    ) {
        super(
        );
        this.Locator = Locator;
    }


    public String getLocator() {
        return Locator;
    }

    public void setLocator(String Locator) {
        this.Locator = Locator;
    }


}