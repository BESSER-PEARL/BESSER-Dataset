





import java.util.List;
import java.util.ArrayList;

public class ddlDsl_SqlNumber extends SqlDataType {

    private int precision;
    private boolean hasPrecision;
    private int scale;



    public ddlDsl_SqlNumber(
        int precision,        boolean hasPrecision,        int scale    ) {
        super(
        );
        this.precision = precision;
        this.hasPrecision = hasPrecision;
        this.scale = scale;
    }


    public int getPrecision() {
        return precision;
    }

    public void setPrecision(int precision) {
        this.precision = precision;
    }
    public boolean getHasprecision() {
        return hasPrecision;
    }

    public void setHasprecision(boolean hasPrecision) {
        this.hasPrecision = hasPrecision;
    }
    public int getScale() {
        return scale;
    }

    public void setScale(int scale) {
        this.scale = scale;
    }


}