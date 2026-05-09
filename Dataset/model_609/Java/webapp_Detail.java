





import java.util.List;
import java.util.ArrayList;

public class webapp_Detail  {

    private int precision;
    private int scale;





    private webapp_Column webapp_column;


    public webapp_Detail(
        int precision,        int scale    ) {
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

    public webapp_Column getWebapp_column() {
        return webapp_column;
    }

    public void setWebapp_column(webapp_Column webapp_column) {
        this.webapp_column = webapp_column;
    }

}