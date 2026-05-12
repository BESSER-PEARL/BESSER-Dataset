





import java.util.List;
import java.util.ArrayList;

public class Hospital  {

    private String HR;
    private String Operation_Theater;
    private String Cariology;



    public Hospital(
        String HR,        String Operation_Theater,        String Cariology    ) {
        this.HR = HR;
        this.Operation_Theater = Operation_Theater;
        this.Cariology = Cariology;
    }


    public String getHr() {
        return HR;
    }

    public void setHr(String HR) {
        this.HR = HR;
    }
    public String getOperation_theater() {
        return Operation_Theater;
    }

    public void setOperation_theater(String Operation_Theater) {
        this.Operation_Theater = Operation_Theater;
    }
    public String getCariology() {
        return Cariology;
    }

    public void setCariology(String Cariology) {
        this.Cariology = Cariology;
    }


}