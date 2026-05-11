





import java.util.List;
import java.util.ArrayList;

public class MARTE_HwTiming_HwTimer extends HwTimingResource {

    private String counterWidth;
    private String nbCounters;



    public MARTE_HwTiming_HwTimer(
        String counterWidth,        String nbCounters    ) {
        super(
        );
        this.counterWidth = counterWidth;
        this.nbCounters = nbCounters;
    }


    public String getCounterwidth() {
        return counterWidth;
    }

    public void setCounterwidth(String counterWidth) {
        this.counterWidth = counterWidth;
    }
    public String getNbcounters() {
        return nbCounters;
    }

    public void setNbcounters(String nbCounters) {
        this.nbCounters = nbCounters;
    }


}