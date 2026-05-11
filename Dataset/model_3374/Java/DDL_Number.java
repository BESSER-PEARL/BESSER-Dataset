





import java.util.List;
import java.util.ArrayList;

public class DDL_Number extends Exacto {

    private int scale;
    private int precision;



    public DDL_Number(
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