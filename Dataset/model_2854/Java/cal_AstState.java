





import java.util.List;
import java.util.ArrayList;

public class cal_AstState  {

    private String name;





    private cal_AstSchedule cal_astschedule;


    public cal_AstState(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public cal_AstSchedule getCal_astschedule() {
        return cal_astschedule;
    }

    public void setCal_astschedule(cal_AstSchedule cal_astschedule) {
        this.cal_astschedule = cal_astschedule;
    }

}