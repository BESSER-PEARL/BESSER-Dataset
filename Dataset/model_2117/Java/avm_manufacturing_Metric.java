





import java.util.List;
import java.util.ArrayList;

public class avm_manufacturing_Metric extends DomainModelMetric {

    private String Name;



    public avm_manufacturing_Metric(
        String Name    ) {
        super(
        );
        this.Name = Name;
    }


    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }


}