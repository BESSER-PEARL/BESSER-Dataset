





import java.util.List;
import java.util.ArrayList;

public class HAL_Depot extends AbstractDepot {

    private String format;



    public HAL_Depot(
        String format    ) {
        super(
        );
        this.format = format;
    }


    public String getFormat() {
        return format;
    }

    public void setFormat(String format) {
        this.format = format;
    }


}