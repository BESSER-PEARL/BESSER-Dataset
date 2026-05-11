





import java.util.List;
import java.util.ArrayList;

public class camel_scalability_Timer  {

    private int timeValue;
    private int maxOccurrenceNum;
    private String type;
    private String name;





    private TimeIntervalUnit timeintervalunit;


    public camel_scalability_Timer(
        int timeValue,        int maxOccurrenceNum,        String type,        String name    ) {
        this.timeValue = timeValue;
        this.maxOccurrenceNum = maxOccurrenceNum;
        this.type = type;
        this.name = name;
    }


    public int getTimevalue() {
        return timeValue;
    }

    public void setTimevalue(int timeValue) {
        this.timeValue = timeValue;
    }
    public int getMaxoccurrencenum() {
        return maxOccurrenceNum;
    }

    public void setMaxoccurrencenum(int maxOccurrenceNum) {
        this.maxOccurrenceNum = maxOccurrenceNum;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public TimeIntervalUnit getTimeintervalunit() {
        return timeintervalunit;
    }

    public void setTimeintervalunit(TimeIntervalUnit timeintervalunit) {
        this.timeintervalunit = timeintervalunit;
    }

}