





import java.util.List;
import java.util.ArrayList;

public class atem_Date extends HeadComponent, SectionElementType {

    private int dsl_Date_month;
    private int dsl_Date_year;
    private int dsl_Date_day;



    public atem_Date(
        int dsl_Date_month,        int dsl_Date_year,        int dsl_Date_day    ) {
        super(
        );
        this.dsl_Date_month = dsl_Date_month;
        this.dsl_Date_year = dsl_Date_year;
        this.dsl_Date_day = dsl_Date_day;
    }


    public int getDsl_date_month() {
        return dsl_Date_month;
    }

    public void setDsl_date_month(int dsl_Date_month) {
        this.dsl_Date_month = dsl_Date_month;
    }
    public int getDsl_date_year() {
        return dsl_Date_year;
    }

    public void setDsl_date_year(int dsl_Date_year) {
        this.dsl_Date_year = dsl_Date_year;
    }
    public int getDsl_date_day() {
        return dsl_Date_day;
    }

    public void setDsl_date_day(int dsl_Date_day) {
        this.dsl_Date_day = dsl_Date_day;
    }


}