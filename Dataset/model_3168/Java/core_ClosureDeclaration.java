





import java.util.List;
import java.util.ArrayList;

public class core_ClosureDeclaration extends Expression {






    private List<core_ClosureParameter> core_closureparameters;


    public core_ClosureDeclaration(
    ) {
        super(
        );
        this.core_closureparameters = new ArrayList<>();
    }

    public core_ClosureDeclaration(
        ArrayList<core_ClosureParameter> core_closureparameters    ) {
        this.core_closureparameters = core_closureparameters;
    }


    public List<core_ClosureParameter> getCore_closureparameters() {
        return core_closureparameters;
    }

    public void addCore_closureparameter(Core_closureparameter core_closureparameter) {
        this.core_closureparameters.add(core_closureparameter);
    }

}