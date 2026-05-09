





import java.util.List;
import java.util.ArrayList;

public class HALL_Geometry_GeometryData2D extends GeometryData {

    private String labelText;



    public HALL_Geometry_GeometryData2D(
        String labelText    ) {
        super(
        );
        this.labelText = labelText;
    }


    public String getLabeltext() {
        return labelText;
    }

    public void setLabeltext(String labelText) {
        this.labelText = labelText;
    }


}