





import java.util.List;
import java.util.ArrayList;

public class DDL_Timestamp extends Times {

    private int precision;



    public DDL_Timestamp(
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