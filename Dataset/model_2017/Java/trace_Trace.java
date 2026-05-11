





import java.util.List;
import java.util.ArrayList;

public class trace_Trace extends EModelElement {

    private String range;
    private String precision;
    private String hostId;



    public trace_Trace(
        String range,        String precision,        String hostId    ) {
        super(
        );
        this.range = range;
        this.precision = precision;
        this.hostId = hostId;
    }


    public String getRange() {
        return range;
    }

    public void setRange(String range) {
        this.range = range;
    }
    public String getPrecision() {
        return precision;
    }

    public void setPrecision(String precision) {
        this.precision = precision;
    }
    public String getHostid() {
        return hostId;
    }

    public void setHostid(String hostId) {
        this.hostId = hostId;
    }


}