





import java.util.List;
import java.util.ArrayList;

public class sql_datatype_ExactNumericType extends NumericType {

    private String scale;
    private String kind;
    private String precision;



    public sql_datatype_ExactNumericType(
        String scale,        String kind,        String precision    ) {
        super(
        );
        this.scale = scale;
        this.kind = kind;
        this.precision = precision;
    }


    public String getScale() {
        return scale;
    }

    public void setScale(String scale) {
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


}