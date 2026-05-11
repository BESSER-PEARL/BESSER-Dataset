





import java.util.List;
import java.util.ArrayList;

public class ioT_FetchDataExpression  {

    private String timeUnit;





    private ioT_FetchData iot_fetchdata;




    private ioT_Time iot_time;


    public ioT_FetchDataExpression(
        String timeUnit    ) {
        this.timeUnit = timeUnit;
    }


    public String getTimeunit() {
        return timeUnit;
    }

    public void setTimeunit(String timeUnit) {
        this.timeUnit = timeUnit;
    }

    public ioT_FetchData getIot_fetchdata() {
        return iot_fetchdata;
    }

    public void setIot_fetchdata(ioT_FetchData iot_fetchdata) {
        this.iot_fetchdata = iot_fetchdata;
    }
    public ioT_Time getIot_time() {
        return iot_time;
    }

    public void setIot_time(ioT_Time iot_time) {
        this.iot_time = iot_time;
    }

}