





import java.util.List;
import java.util.ArrayList;

public class ioT_Time  {

    private int time;





    private ioT_FetchDataExpression iot_fetchdataexpression;


    public ioT_Time(
        int time    ) {
        this.time = time;
    }


    public int getTime() {
        return time;
    }

    public void setTime(int time) {
        this.time = time;
    }

    public ioT_FetchDataExpression getIot_fetchdataexpression() {
        return iot_fetchdataexpression;
    }

    public void setIot_fetchdataexpression(ioT_FetchDataExpression iot_fetchdataexpression) {
        this.iot_fetchdataexpression = iot_fetchdataexpression;
    }

}