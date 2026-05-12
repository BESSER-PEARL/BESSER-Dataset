





import java.util.List;
import java.util.ArrayList;

public class Hospital  {

    private String Cardiology;
    private String Cancer_Center;
    private String Operation_Theater;
    private String HR;



    public Hospital(
        String Cardiology,        String Cancer_Center,        String Operation_Theater,        String HR    ) {
        this.Cardiology = Cardiology;
        this.Cancer_Center = Cancer_Center;
        this.Operation_Theater = Operation_Theater;
        this.HR = HR;
    }


    public String getCardiology() {
        return Cardiology;
    }

    public void setCardiology(String Cardiology) {
        this.Cardiology = Cardiology;
    }
    public String getCancer_center() {
        return Cancer_Center;
    }

    public void setCancer_center(String Cancer_Center) {
        this.Cancer_Center = Cancer_Center;
    }
    public String getOperation_theater() {
        return Operation_Theater;
    }

    public void setOperation_theater(String Operation_Theater) {
        this.Operation_Theater = Operation_Theater;
    }
    public String getHr() {
        return HR;
    }

    public void setHr(String HR) {
        this.HR = HR;
    }


}