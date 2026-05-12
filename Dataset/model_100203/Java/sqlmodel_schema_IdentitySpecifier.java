





import java.util.List;
import java.util.ArrayList;

public class sqlmodel_schema_IdentitySpecifier extends SQLObject {

    private boolean cycleOption;
    private String generationType;
    private String maximum;
    private String increment;
    private String minimum;
    private String startValue;



    public sqlmodel_schema_IdentitySpecifier(
        boolean cycleOption,        String generationType,        String maximum,        String increment,        String minimum,        String startValue    ) {
        super(
        );
        this.cycleOption = cycleOption;
        this.generationType = generationType;
        this.maximum = maximum;
        this.increment = increment;
        this.minimum = minimum;
        this.startValue = startValue;
    }


    public boolean getCycleoption() {
        return cycleOption;
    }

    public void setCycleoption(boolean cycleOption) {
        this.cycleOption = cycleOption;
    }
    public String getGenerationtype() {
        return generationType;
    }

    public void setGenerationtype(String generationType) {
        this.generationType = generationType;
    }
    public String getMaximum() {
        return maximum;
    }

    public void setMaximum(String maximum) {
        this.maximum = maximum;
    }
    public String getIncrement() {
        return increment;
    }

    public void setIncrement(String increment) {
        this.increment = increment;
    }
    public String getMinimum() {
        return minimum;
    }

    public void setMinimum(String minimum) {
        this.minimum = minimum;
    }
    public String getStartvalue() {
        return startValue;
    }

    public void setStartvalue(String startValue) {
        this.startValue = startValue;
    }


}