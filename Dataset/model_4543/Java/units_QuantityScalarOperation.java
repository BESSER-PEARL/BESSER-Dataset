





import java.util.List;
import java.util.ArrayList;

public class units_QuantityScalarOperation extends QuantityOperation {

    private float rhs;





    private units_Quantity units_quantity;


    public units_QuantityScalarOperation(
        float rhs    ) {
        super(
        );
        this.rhs = rhs;
    }


    public float getRhs() {
        return rhs;
    }

    public void setRhs(float rhs) {
        this.rhs = rhs;
    }

    public units_Quantity getUnits_quantity() {
        return units_quantity;
    }

    public void setUnits_quantity(units_Quantity units_quantity) {
        this.units_quantity = units_quantity;
    }

}