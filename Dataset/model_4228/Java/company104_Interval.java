





import java.util.List;
import java.util.ArrayList;

public class company104_Interval  {

    private String dateTo;
    private String dateFrom;



    public company104_Interval(
        String dateTo,        String dateFrom    ) {
        this.dateTo = dateTo;
        this.dateFrom = dateFrom;
    }


    public String getDateto() {
        return dateTo;
    }

    public void setDateto(String dateTo) {
        this.dateTo = dateTo;
    }
    public String getDatefrom() {
        return dateFrom;
    }

    public void setDatefrom(String dateFrom) {
        this.dateFrom = dateFrom;
    }


}