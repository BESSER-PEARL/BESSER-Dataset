





import java.util.List;
import java.util.ArrayList;

public class ddlDsl_SqlInterval extends SqlDateTime {

    private int precision;
    private boolean year;
    private int secondsPrecision;
    private boolean day;



    public ddlDsl_SqlInterval(
        int precision,        boolean year,        int secondsPrecision,        boolean day    ) {
        super(
        );
        this.precision = precision;
        this.year = year;
        this.secondsPrecision = secondsPrecision;
        this.day = day;
    }


    public int getPrecision() {
        return precision;
    }

    public void setPrecision(int precision) {
        this.precision = precision;
    }
    public boolean getYear() {
        return year;
    }

    public void setYear(boolean year) {
        this.year = year;
    }
    public int getSecondsprecision() {
        return secondsPrecision;
    }

    public void setSecondsprecision(int secondsPrecision) {
        this.secondsPrecision = secondsPrecision;
    }
    public boolean getDay() {
        return day;
    }

    public void setDay(boolean day) {
        this.day = day;
    }


}