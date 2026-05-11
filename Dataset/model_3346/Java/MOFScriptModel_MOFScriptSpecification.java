





import java.util.List;
import java.util.ArrayList;

public class MOFScriptModel_MOFScriptSpecification extends MOFScriptObject {






    private List<MOFScriptModel_MOFScriptTransformation> mofscriptmodel_mofscripttransformations;




    private List<MOFScriptModel_MOFScriptImport> mofscriptmodel_mofscriptimports;


    public MOFScriptModel_MOFScriptSpecification(
    ) {
        super(
        );
        this.mofscriptmodel_mofscripttransformations = new ArrayList<>();
        this.mofscriptmodel_mofscriptimports = new ArrayList<>();
    }

    public MOFScriptModel_MOFScriptSpecification(
        ArrayList<MOFScriptModel_MOFScriptTransformation> mofscriptmodel_mofscripttransformations,        ArrayList<MOFScriptModel_MOFScriptImport> mofscriptmodel_mofscriptimports    ) {
        this.mofscriptmodel_mofscripttransformations = mofscriptmodel_mofscripttransformations;
        this.mofscriptmodel_mofscriptimports = mofscriptmodel_mofscriptimports;
    }


    public List<MOFScriptModel_MOFScriptTransformation> getMofscriptmodel_mofscripttransformations() {
        return mofscriptmodel_mofscripttransformations;
    }

    public void addMofscriptmodel_mofscripttransformation(Mofscriptmodel_mofscripttransformation mofscriptmodel_mofscripttransformation) {
        this.mofscriptmodel_mofscripttransformations.add(mofscriptmodel_mofscripttransformation);
    }
    public List<MOFScriptModel_MOFScriptImport> getMofscriptmodel_mofscriptimports() {
        return mofscriptmodel_mofscriptimports;
    }

    public void addMofscriptmodel_mofscriptimport(Mofscriptmodel_mofscriptimport mofscriptmodel_mofscriptimport) {
        this.mofscriptmodel_mofscriptimports.add(mofscriptmodel_mofscriptimport);
    }

}