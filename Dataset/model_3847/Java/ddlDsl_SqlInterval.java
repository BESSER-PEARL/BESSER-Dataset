





import java.util.List;
import java.util.ArrayList;

public class ddlDsl_SqlInterval extends SqlDateTime {

    private int secondsPrecision;
    private boolean day;
    private boolean year;
    private int precision;



    public ddlDsl_SqlInterval(
        int secondsPrecision,        boolean day,        boolean year,        int precision    ) {
        super(
        );
        this.secondsPrecision = secondsPrecision;
        this.day = day;
        this.year = year;
        this.precision = precision;
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
    public boolean getYear() {
        return year;
    }

    public void setYear(boolean year) {
        this.year = year;
    }
    public int getPrecision() {
        return precision;
    }

    public void setPrecision(int precision) {
        this.precision = precision;
    }


}