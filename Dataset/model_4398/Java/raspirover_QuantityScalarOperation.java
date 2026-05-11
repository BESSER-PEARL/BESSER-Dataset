





import java.util.List;
import java.util.ArrayList;

public class raspirover_QuantityScalarOperation extends QuantityOperation {

    private float rhs;





    private raspirover_Quantity raspirover_quantity;


    public raspirover_QuantityScalarOperation(
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

    public raspirover_Quantity getRaspirover_quantity() {
        return raspirover_quantity;
    }

    public void setRaspirover_quantity(raspirover_Quantity raspirover_quantity) {
        this.raspirover_quantity = raspirover_quantity;
    }

}