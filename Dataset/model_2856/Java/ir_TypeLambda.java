





import java.util.List;
import java.util.ArrayList;

public class ir_TypeLambda extends Type {






    private ir_Type ir_type;




    private List<ir_Type> ir_types;


    public ir_TypeLambda(
    ) {
        super(
        );
        this.ir_types = new ArrayList<>();
    }

    public ir_TypeLambda(
        ArrayList<ir_Type> ir_types    ) {
        this.ir_types = ir_types;
    }


    public ir_Type getIr_type() {
        return ir_type;
    }

    public void setIr_type(ir_Type ir_type) {
        this.ir_type = ir_type;
    }
    public List<ir_Type> getIr_types() {
        return ir_types;
    }

    public void addIr_type(Ir_type ir_type) {
        this.ir_types.add(ir_type);
    }

}