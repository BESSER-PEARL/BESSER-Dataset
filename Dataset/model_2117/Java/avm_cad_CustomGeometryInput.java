





import java.util.List;
import java.util.ArrayList;

public class avm_cad_CustomGeometryInput  {

    private String Operation;





    private Geometry geometry;


    public avm_cad_CustomGeometryInput(
        String Operation    ) {
        this.Operation = Operation;
    }


    public String getOperation() {
        return Operation;
    }

    public void setOperation(String Operation) {
        this.Operation = Operation;
    }

    public Geometry getGeometry() {
        return geometry;
    }

    public void setGeometry(Geometry geometry) {
        this.geometry = geometry;
    }

}