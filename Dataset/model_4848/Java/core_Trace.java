





import java.util.List;
import java.util.ArrayList;

public class core_Trace extends ReferencedModelElements {






    private List<core_Specification> core_specifications;


    public core_Trace(
    ) {
        super(
        );
        this.core_specifications = new ArrayList<>();
    }

    public core_Trace(
        ArrayList<core_Specification> core_specifications    ) {
        this.core_specifications = core_specifications;
    }


    public List<core_Specification> getCore_specifications() {
        return core_specifications;
    }

    public void addCore_specification(Core_specification core_specification) {
        this.core_specifications.add(core_specification);
    }

}