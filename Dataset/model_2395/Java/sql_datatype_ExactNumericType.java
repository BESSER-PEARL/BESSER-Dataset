





import java.util.List;
import java.util.ArrayList;

public class sql_datatype_ExactNumericType extends NumericType {

    private String kind;
    private String precision;
    private String scale;



    public sql_datatype_ExactNumericType(
        String kind,        String precision,        String scale    ) {
        super(
        );
        this.kind = kind;
        this.precision = precision;
        this.scale = scale;
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
    public String getScale() {
        return scale;
    }

    public void setScale(String scale) {
        this.scale = scale;
    }


}