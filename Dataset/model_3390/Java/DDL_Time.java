





import java.util.List;
import java.util.ArrayList;

public class DDL_Time extends DatetimeType {

    private boolean withTimeZone;
    private int precision;



    public DDL_Time(
        boolean withTimeZone,        int precision    ) {
        super(
        );
        this.withTimeZone = withTimeZone;
        this.precision = precision;
    }


    public boolean getWithtimezone() {
        return withTimeZone;
    }

    public void setWithtimezone(boolean withTimeZone) {
        this.withTimeZone = withTimeZone;
    }
    public int getPrecision() {
        return precision;
    }

    public void setPrecision(int precision) {
        this.precision = precision;
    }


}