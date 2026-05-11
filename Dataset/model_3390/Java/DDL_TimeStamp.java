





import java.util.List;
import java.util.ArrayList;

public class DDL_TimeStamp extends DatetimeType {

    private int precision;
    private boolean withTimeZone;



    public DDL_TimeStamp(
        int precision,        boolean withTimeZone    ) {
        super(
        );
        this.precision = precision;
        this.withTimeZone = withTimeZone;
    }


    public int getPrecision() {
        return precision;
    }

    public void setPrecision(int precision) {
        this.precision = precision;
    }
    public boolean getWithtimezone() {
        return withTimeZone;
    }

    public void setWithtimezone(boolean withTimeZone) {
        this.withTimeZone = withTimeZone;
    }


}