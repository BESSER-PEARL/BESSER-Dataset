





import java.util.List;
import java.util.ArrayList;

public class eel_MeasureOCL extends MeasureValue {

    private String oclQuery;



    public eel_MeasureOCL(
        String oclQuery    ) {
        super(
        );
        this.oclQuery = oclQuery;
    }


    public String getOclquery() {
        return oclQuery;
    }

    public void setOclquery(String oclQuery) {
        this.oclQuery = oclQuery;
    }


}