





import java.util.List;
import java.util.ArrayList;

public class farmbot_modeling_Schedule extends Command {

    private String endTime;
    private String startTime;
    private String startDate;
    private boolean repeat;
    private String repeatUnit;
    private String endDate;
    private int sequence;



    public farmbot_modeling_Schedule(
        String endTime,        String startTime,        String startDate,        boolean repeat,        String repeatUnit,        String endDate,        int sequence    ) {
        super(
        );
        this.endTime = endTime;
        this.startTime = startTime;
        this.startDate = startDate;
        this.repeat = repeat;
        this.repeatUnit = repeatUnit;
        this.endDate = endDate;
        this.sequence = sequence;
    }


    public String getEndtime() {
        return endTime;
    }

    public void setEndtime(String endTime) {
        this.endTime = endTime;
    }
    public String getStarttime() {
        return startTime;
    }

    public void setStarttime(String startTime) {
        this.startTime = startTime;
    }
    public String getStartdate() {
        return startDate;
    }

    public void setStartdate(String startDate) {
        this.startDate = startDate;
    }
    public boolean getRepeat() {
        return repeat;
    }

    public void setRepeat(boolean repeat) {
        this.repeat = repeat;
    }
    public String getRepeatunit() {
        return repeatUnit;
    }

    public void setRepeatunit(String repeatUnit) {
        this.repeatUnit = repeatUnit;
    }
    public String getEnddate() {
        return endDate;
    }

    public void setEnddate(String endDate) {
        this.endDate = endDate;
    }
    public int getSequence() {
        return sequence;
    }

    public void setSequence(int sequence) {
        this.sequence = sequence;
    }


}