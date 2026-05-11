





import java.util.List;
import java.util.ArrayList;

public class DDL_Decimal extends ExactNumericType {

    private int scale;
    private int precision;



    public DDL_Decimal(
        int scale,        int precision    ) {
        super(
        );
        this.scale = scale;
        this.precision = precision;
    }


    public int getScale() {
        return scale;
    }

    public void setScale(int scale) {
        this.scale = scale;
    }
    public int getPrecision() {
        return precision;
    }

    public void setPrecision(int precision) {
        this.precision = precision;
    }


}