





import java.util.List;
import java.util.ArrayList;

public class roverDSL_BSensorLiteral extends ValueExpression {

    private String sensor;



    public roverDSL_BSensorLiteral(
        String sensor    ) {
        super(
        );
        this.sensor = sensor;
    }


    public String getSensor() {
        return sensor;
    }

    public void setSensor(String sensor) {
        this.sensor = sensor;
    }


}