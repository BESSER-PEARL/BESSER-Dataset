





import java.util.List;
import java.util.ArrayList;

public class CWMRelationalData_SQLDistinctType extends SQLDataType {

    private String scale;
    private String precision;
    private String length;



    public CWMRelationalData_SQLDistinctType(
        String scale,        String precision,        String length    ) {
        super(
        );
        this.scale = scale;
        this.precision = precision;
        this.length = length;
    }


    public String getScale() {
        return scale;
    }

    public void setScale(String scale) {
        this.scale = scale;
    }
    public String getPrecision() {
        return precision;
    }

    public void setPrecision(String precision) {
        this.precision = precision;
    }
    public String getLength() {
        return length;
    }

    public void setLength(String length) {
        this.length = length;
    }


}