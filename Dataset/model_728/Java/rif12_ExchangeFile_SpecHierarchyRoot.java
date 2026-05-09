





import java.util.List;
import java.util.ArrayList;

public class rif12_ExchangeFile_SpecHierarchyRoot extends SpecElementWithUserDefinedAttributes {






    private List<SpecHierarchy> spechierarchys;


    public rif12_ExchangeFile_SpecHierarchyRoot(
    ) {
        super(
        );
        this.spechierarchys = new ArrayList<>();
    }

    public rif12_ExchangeFile_SpecHierarchyRoot(
        ArrayList<SpecHierarchy> spechierarchys    ) {
        this.spechierarchys = spechierarchys;
    }


    public List<SpecHierarchy> getSpechierarchys() {
        return spechierarchys;
    }

    public void addSpechierarchy(Spechierarchy spechierarchy) {
        this.spechierarchys.add(spechierarchy);
    }

}