





import java.util.List;
import java.util.ArrayList;

public class sql_datatype_TimestampType extends DatetimeType {

    private String precision;
    private String withTimeZone;



    public sql_datatype_TimestampType(
        String precision,        String withTimeZone    ) {
        super(
        );
        this.precision = precision;
        this.withTimeZone = withTimeZone;
    }


    public String getPrecision() {
        return precision;
    }

    public void setPrecision(String precision) {
        this.precision = precision;
    }
    public String getWithtimezone() {
        return withTimeZone;
    }

    public void setWithtimezone(String withTimeZone) {
        this.withTimeZone = withTimeZone;
    }


}