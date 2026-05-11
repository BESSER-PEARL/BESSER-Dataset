





import java.util.List;
import java.util.ArrayList;

public class MARTE_RSM_InterRepetition extends LinkTopology {

    private String repetitionShapeDependence;
    private String isModulo;



    public MARTE_RSM_InterRepetition(
        String repetitionShapeDependence,        String isModulo    ) {
        super(
        );
        this.repetitionShapeDependence = repetitionShapeDependence;
        this.isModulo = isModulo;
    }


    public String getRepetitionshapedependence() {
        return repetitionShapeDependence;
    }

    public void setRepetitionshapedependence(String repetitionShapeDependence) {
        this.repetitionShapeDependence = repetitionShapeDependence;
    }
    public String getIsmodulo() {
        return isModulo;
    }

    public void setIsmodulo(String isModulo) {
        this.isModulo = isModulo;
    }


}