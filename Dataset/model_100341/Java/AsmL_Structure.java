





import java.util.List;
import java.util.ArrayList;

public class AsmL_Structure extends AsmLElement {

    private String name;
    private String superStructureName;



    public AsmL_Structure(
        String name,        String superStructureName    ) {
        super(
        );
        this.name = name;
        this.superStructureName = superStructureName;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getSuperstructurename() {
        return superStructureName;
    }

    public void setSuperstructurename(String superStructureName) {
        this.superStructureName = superStructureName;
    }


}