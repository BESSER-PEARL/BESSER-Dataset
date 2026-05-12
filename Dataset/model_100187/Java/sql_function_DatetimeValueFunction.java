





import java.util.List;
import java.util.ArrayList;

public class sql_function_DatetimeValueFunction  {

    private String precision;
    private String kind;



    public sql_function_DatetimeValueFunction(
        String precision,        String kind    ) {
        this.precision = precision;
        this.kind = kind;
    }


    public String getPrecision() {
        return precision;
    }

    public void setPrecision(String precision) {
        this.precision = precision;
    }
    public String getKind() {
        return kind;
    }

    public void setKind(String kind) {
        this.kind = kind;
    }


}