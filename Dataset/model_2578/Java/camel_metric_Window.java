





import java.util.List;
import java.util.ArrayList;

public class camel_metric_Window  {

    private String measurementSize;
    private String name;
    private String timeSize;
    private String windowType;
    private String sizeType;





    private TimeIntervalUnit timeintervalunit;


    public camel_metric_Window(
        String measurementSize,        String name,        String timeSize,        String windowType,        String sizeType    ) {
        this.measurementSize = measurementSize;
        this.name = name;
        this.timeSize = timeSize;
        this.windowType = windowType;
        this.sizeType = sizeType;
    }


    public String getMeasurementsize() {
        return measurementSize;
    }

    public void setMeasurementsize(String measurementSize) {
        this.measurementSize = measurementSize;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getTimesize() {
        return timeSize;
    }

    public void setTimesize(String timeSize) {
        this.timeSize = timeSize;
    }
    public String getWindowtype() {
        return windowType;
    }

    public void setWindowtype(String windowType) {
        this.windowType = windowType;
    }
    public String getSizetype() {
        return sizeType;
    }

    public void setSizetype(String sizeType) {
        this.sizeType = sizeType;
    }

    public TimeIntervalUnit getTimeintervalunit() {
        return timeintervalunit;
    }

    public void setTimeintervalunit(TimeIntervalUnit timeintervalunit) {
        this.timeintervalunit = timeintervalunit;
    }

}