





import java.util.List;
import java.util.ArrayList;

public class ddlDsl_SqlTimeStamp extends SqlDateTime {

    private int precision;



    public ddlDsl_SqlTimeStamp(
        int precision    ) {
        super(
        );
        this.precision = precision;
    }


    public int getPrecision() {
        return precision;
    }

    public void setPrecision(int precision) {
        this.precision = precision;
    }


}