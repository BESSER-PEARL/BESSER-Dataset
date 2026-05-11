





import java.util.List;
import java.util.ArrayList;

public class ddlDsl_SqlNumber extends SqlDataType {

    private int scale;
    private int precision;
    private boolean hasPrecision;



    public ddlDsl_SqlNumber(
        int scale,        int precision,        boolean hasPrecision    ) {
        super(
        );
        this.scale = scale;
        this.precision = precision;
        this.hasPrecision = hasPrecision;
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
    public boolean getHasprecision() {
        return hasPrecision;
    }

    public void setHasprecision(boolean hasPrecision) {
        this.hasPrecision = hasPrecision;
    }


}