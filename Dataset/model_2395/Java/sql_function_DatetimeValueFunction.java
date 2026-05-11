





import java.util.List;
import java.util.ArrayList;

public class sql_function_DatetimeValueFunction  {

    private String kind;
    private String precision;



    public sql_function_DatetimeValueFunction(
        String kind,        String precision    ) {
        this.kind = kind;
        this.precision = precision;
    }


    public String getKind() {
        return kind;
    }

    public void setKind(String kind) {
        this.kind = kind;
    }
    public String getPrecision() {
        return precision;
    }

    public void setPrecision(String precision) {
        this.precision = precision;
    }


}