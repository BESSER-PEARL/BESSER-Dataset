





import java.util.List;
import java.util.ArrayList;

public class avm_SecurityClassification extends DistributionRestriction {

    private String Level;



    public avm_SecurityClassification(
        String Level    ) {
        super(
        );
        this.Level = Level;
    }


    public String getLevel() {
        return Level;
    }

    public void setLevel(String Level) {
        this.Level = Level;
    }


}