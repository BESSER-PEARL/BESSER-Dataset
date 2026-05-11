





import java.util.List;
import java.util.ArrayList;

public class database_Sequence extends NamedElement {

    private String minValue;
    private String cacheSize;
    private String maxValue;
    private boolean cycle;
    private String increment;
    private String start;



    public database_Sequence(
        String minValue,        String cacheSize,        String maxValue,        boolean cycle,        String increment,        String start    ) {
        super(
        );
        this.minValue = minValue;
        this.cacheSize = cacheSize;
        this.maxValue = maxValue;
        this.cycle = cycle;
        this.increment = increment;
        this.start = start;
    }


    public String getMinvalue() {
        return minValue;
    }

    public void setMinvalue(String minValue) {
        this.minValue = minValue;
    }
    public String getCachesize() {
        return cacheSize;
    }

    public void setCachesize(String cacheSize) {
        this.cacheSize = cacheSize;
    }
    public String getMaxvalue() {
        return maxValue;
    }

    public void setMaxvalue(String maxValue) {
        this.maxValue = maxValue;
    }
    public boolean getCycle() {
        return cycle;
    }

    public void setCycle(boolean cycle) {
        this.cycle = cycle;
    }
    public String getIncrement() {
        return increment;
    }

    public void setIncrement(String increment) {
        this.increment = increment;
    }
    public String getStart() {
        return start;
    }

    public void setStart(String start) {
        this.start = start;
    }


}