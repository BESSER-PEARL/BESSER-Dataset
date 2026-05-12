





import java.util.List;
import java.util.ArrayList;

public class ddlDsl_SqlInterval extends SqlDateTime {

    private boolean day;
    private boolean year;
    private int secondsPrecision;
    private int precision;



    public ddlDsl_SqlInterval(
        boolean day,        boolean year,        int secondsPrecision,        int precision    ) {
        super(
        );
        this.day = day;
        this.year = year;
        this.secondsPrecision = secondsPrecision;
        this.precision = precision;
    }


    public boolean getDay() {
        return day;
    }

    public void setDay(boolean day) {
        this.day = day;
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
    public int getPrecision() {
        return precision;
    }

    public void setPrecision(int precision) {
        this.precision = precision;
    }


}