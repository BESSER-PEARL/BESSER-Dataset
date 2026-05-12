





import java.util.List;
import java.util.ArrayList;

public class HAL_DepotWeb extends AbstractDepot {

    private String format;



    public HAL_DepotWeb(
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