





import java.util.List;
import java.util.ArrayList;

public class build_context_IResolution  {






    private ImportOptions importoptions;




    private List<IResolution> iresolutions;


    public build_context_IResolution(
    ) {
        this.iresolutions = new ArrayList<>();
    }

    public build_context_IResolution(
        ArrayList<IResolution> iresolutions    ) {
        this.iresolutions = iresolutions;
    }


    public ImportOptions getImportoptions() {
        return importoptions;
    }

    public void setImportoptions(ImportOptions importoptions) {
        this.importoptions = importoptions;
    }
    public List<IResolution> getIresolutions() {
        return iresolutions;
    }

    public void addIresolution(Iresolution iresolution) {
        this.iresolutions.add(iresolution);
    }

}