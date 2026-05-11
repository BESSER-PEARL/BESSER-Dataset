





import java.util.List;
import java.util.ArrayList;

public class afpText_LocalDateAndTimeStamp extends triplet {

    private String Second;
    private String TenYear;
    private String Hour;
    private String THunYear;
    private String HundSec;
    private String StampType;
    private String Day;
    private String Minute;



    public afpText_LocalDateAndTimeStamp(
        String Second,        String TenYear,        String Hour,        String THunYear,        String HundSec,        String StampType,        String Day,        String Minute    ) {
        super(
        );
        this.Second = Second;
        this.TenYear = TenYear;
        this.Hour = Hour;
        this.THunYear = THunYear;
        this.HundSec = HundSec;
        this.StampType = StampType;
        this.Day = Day;
        this.Minute = Minute;
    }


    public String getSecond() {
        return Second;
    }

    public void setSecond(String Second) {
        this.Second = Second;
    }
    public String getTenyear() {
        return TenYear;
    }

    public void setTenyear(String TenYear) {
        this.TenYear = TenYear;
    }
    public String getHour() {
        return Hour;
    }

    public void setHour(String Hour) {
        this.Hour = Hour;
    }
    public String getThunyear() {
        return THunYear;
    }

    public void setThunyear(String THunYear) {
        this.THunYear = THunYear;
    }
    public String getHundsec() {
        return HundSec;
    }

    public void setHundsec(String HundSec) {
        this.HundSec = HundSec;
    }
    public String getStamptype() {
        return StampType;
    }

    public void setStamptype(String StampType) {
        this.StampType = StampType;
    }
    public String getDay() {
        return Day;
    }

    public void setDay(String Day) {
        this.Day = Day;
    }
    public String getMinute() {
        return Minute;
    }

    public void setMinute(String Minute) {
        this.Minute = Minute;
    }


}