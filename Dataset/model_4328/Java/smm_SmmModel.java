





import java.util.List;
import java.util.ArrayList;

public class smm_SmmModel extends SmmElement {






    private List<smm_MeasureLibrary> smm_measurelibrarys;


    public smm_SmmModel(
    ) {
        super(
        );
        this.smm_measurelibrarys = new ArrayList<>();
    }

    public smm_SmmModel(
        ArrayList<smm_MeasureLibrary> smm_measurelibrarys    ) {
        this.smm_measurelibrarys = smm_measurelibrarys;
    }


    public List<smm_MeasureLibrary> getSmm_measurelibrarys() {
        return smm_measurelibrarys;
    }

    public void addSmm_measurelibrary(Smm_measurelibrary smm_measurelibrary) {
        this.smm_measurelibrarys.add(smm_measurelibrary);
    }

}