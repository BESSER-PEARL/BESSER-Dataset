





import java.util.List;
import java.util.ArrayList;

public class database_Sequence extends NamedElement {

    private String start;
    private String cacheSize;
    private String minValue;
    private String maxValue;
    private boolean cycle;
    private String increment;



    public database_Sequence(
        String start,        String cacheSize,        String minValue,        String maxValue,        boolean cycle,        String increment    ) {
        super(
        );
        this.start = start;
        this.cacheSize = cacheSize;
        this.minValue = minValue;
        this.maxValue = maxValue;
        this.cycle = cycle;
        this.increment = increment;
    }


    public String getStart() {
        return start;
    }

    public void setStart(String start) {
        this.start = start;
    }
    public String getCachesize() {
        return cacheSize;
    }

    public void setCachesize(String cacheSize) {
        this.cacheSize = cacheSize;
    }
    public String getMinvalue() {
        return minValue;
    }

    public void setMinvalue(String minValue) {
        this.minValue = minValue;
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


}