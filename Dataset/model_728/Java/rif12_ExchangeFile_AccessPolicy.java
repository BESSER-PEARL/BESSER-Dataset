





import java.util.List;
import java.util.ArrayList;

public class rif12_ExchangeFile_AccessPolicy extends Identifiable {

    private String accessMode;





    private List<SpecHierarchy> spechierarchys;


    public rif12_ExchangeFile_AccessPolicy(
        String accessMode    ) {
        super(
        );
        this.accessMode = accessMode;
        this.spechierarchys = new ArrayList<>();
    }

    public rif12_ExchangeFile_AccessPolicy(
        String accessMode        ArrayList<SpecHierarchy> spechierarchys    ) {
        this.accessMode = accessMode;
        this.spechierarchys = spechierarchys;
    }

    public String getAccessmode() {
        return accessMode;
    }

    public void setAccessmode(String accessMode) {
        this.accessMode = accessMode;
    }

    public List<SpecHierarchy> getSpechierarchys() {
        return spechierarchys;
    }

    public void addSpechierarchy(Spechierarchy spechierarchy) {
        this.spechierarchys.add(spechierarchy);
    }

}