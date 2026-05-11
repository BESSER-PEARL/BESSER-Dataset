





import java.util.List;
import java.util.ArrayList;

public class DDL_Decimal extends ExactNumericType {

    private int precision;
    private int scale;



    public DDL_Decimal(
        int precision,        int scale    ) {
        super(
        );
        this.precision = precision;
        this.scale = scale;
    }


    public int getPrecision() {
        return precision;
    }

    public void setPrecision(int precision) {
        this.precision = precision;
    }
    public int getScale() {
        return scale;
    }

    public void setScale(int scale) {
        this.scale = scale;
    }


}