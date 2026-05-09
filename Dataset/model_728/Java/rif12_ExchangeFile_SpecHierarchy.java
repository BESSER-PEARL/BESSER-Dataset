





import java.util.List;
import java.util.ArrayList;

public class rif12_ExchangeFile_SpecHierarchy extends Identifiable {






    private List<SpecHierarchy> spechierarchys;


    public rif12_ExchangeFile_SpecHierarchy(
    ) {
        super(
        );
        this.spechierarchys = new ArrayList<>();
    }

    public rif12_ExchangeFile_SpecHierarchy(
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