





import java.util.List;
import java.util.ArrayList;

public class DDL_Float extends Aproximado {

    private int precision;



    public DDL_Float(
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