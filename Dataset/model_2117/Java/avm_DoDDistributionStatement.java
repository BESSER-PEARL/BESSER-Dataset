





import java.util.List;
import java.util.ArrayList;

public class avm_DoDDistributionStatement extends DistributionRestriction {

    private String Type;



    public avm_DoDDistributionStatement(
        String Type    ) {
        super(
        );
        this.Type = Type;
    }


    public String getType() {
        return Type;
    }

    public void setType(String Type) {
        this.Type = Type;
    }


}