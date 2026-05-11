





import java.util.List;
import java.util.ArrayList;

public class ddlDsl_SqlNumber extends SqlDataType {

    private boolean hasPrecision;
    private int precision;
    private int scale;



    public ddlDsl_SqlNumber(
        boolean hasPrecision,        int precision,        int scale    ) {
        super(
        );
        this.hasPrecision = hasPrecision;
        this.precision = precision;
        this.scale = scale;
    }


    public boolean getHasprecision() {
        return hasPrecision;
    }

    public void setHasprecision(boolean hasPrecision) {
        this.hasPrecision = hasPrecision;
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