





import java.util.List;
import java.util.ArrayList;

public class ir_Namespace extends Scope {

    private String name;





    private List<ir_AbstractActor> ir_abstractactors;


    public ir_Namespace(
        String name    ) {
        super(
        );
        this.name = name;
        this.ir_abstractactors = new ArrayList<>();
    }

    public ir_Namespace(
        String name        ArrayList<ir_AbstractActor> ir_abstractactors    ) {
        this.name = name;
        this.ir_abstractactors = ir_abstractactors;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<ir_AbstractActor> getIr_abstractactors() {
        return ir_abstractactors;
    }

    public void addIr_abstractactor(Ir_abstractactor ir_abstractactor) {
        this.ir_abstractactors.add(ir_abstractactor);
    }

}