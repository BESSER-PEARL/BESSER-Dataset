





import java.util.List;
import java.util.ArrayList;

public class afpText_UniversalDateAndTimeStamp extends triplet {

    private String UTCDiffH;
    private String Month;
    private String YearAD;
    private String Second;
    private String Hour;
    private String TimeZone;
    private String Minute;
    private String Reserved;
    private String Day;
    private String UTCDiffM;



    public afpText_UniversalDateAndTimeStamp(
        String UTCDiffH,        String Month,        String YearAD,        String Second,        String Hour,        String TimeZone,        String Minute,        String Reserved,        String Day,        String UTCDiffM    ) {
        super(
        );
        this.UTCDiffH = UTCDiffH;
        this.Month = Month;
        this.YearAD = YearAD;
        this.Second = Second;
        this.Hour = Hour;
        this.TimeZone = TimeZone;
        this.Minute = Minute;
        this.Reserved = Reserved;
        this.Day = Day;
        this.UTCDiffM = UTCDiffM;
    }


    public String getUtcdiffh() {
        return UTCDiffH;
    }

    public void setUtcdiffh(String UTCDiffH) {
        this.UTCDiffH = UTCDiffH;
    }
    public String getMonth() {
        return Month;
    }

    public void setMonth(String Month) {
        this.Month = Month;
    }
    public String getYearad() {
        return YearAD;
    }

    public void setYearad(String YearAD) {
        this.YearAD = YearAD;
    }
    public String getSecond() {
        return Second;
    }

    public void setSecond(String Second) {
        this.Second = Second;
    }
    public String getHour() {
        return Hour;
    }

    public void setHour(String Hour) {
        this.Hour = Hour;
    }
    public String getTimezone() {
        return TimeZone;
    }

    public void setTimezone(String TimeZone) {
        this.TimeZone = TimeZone;
    }
    public String getMinute() {
        return Minute;
    }

    public void setMinute(String Minute) {
        this.Minute = Minute;
    }
    public String getReserved() {
        return Reserved;
    }

    public void setReserved(String Reserved) {
        this.Reserved = Reserved;
    }
    public String getDay() {
        return Day;
    }

    public void setDay(String Day) {
        this.Day = Day;
    }
    public String getUtcdiffm() {
        return UTCDiffM;
    }

    public void setUtcdiffm(String UTCDiffM) {
        this.UTCDiffM = UTCDiffM;
    }


}