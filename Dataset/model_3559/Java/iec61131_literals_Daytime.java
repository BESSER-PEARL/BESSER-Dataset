





import java.util.List;
import java.util.ArrayList;

public class iec61131_literals_Daytime  {

    private String minute;
    private String hour;





    private Fixed_Point fixed_point;


    public iec61131_literals_Daytime(
        String minute,        String hour    ) {
        this.minute = minute;
        this.hour = hour;
    }


    public String getMinute() {
        return minute;
    }

    public void setMinute(String minute) {
        this.minute = minute;
    }
    public String getHour() {
        return hour;
    }

    public void setHour(String hour) {
        this.hour = hour;
    }

    public Fixed_Point getFixed_point() {
        return fixed_point;
    }

    public void setFixed_point(Fixed_Point fixed_point) {
        this.fixed_point = fixed_point;
    }

}