





import java.util.List;
import java.util.ArrayList;

public class MOFScriptModel_MOFScriptAspect extends MOFScriptTransformation {






    private List<MOFScriptModel_Advice> mofscriptmodel_advices;


    public MOFScriptModel_MOFScriptAspect(
    ) {
        super(
        );
        this.mofscriptmodel_advices = new ArrayList<>();
    }

    public MOFScriptModel_MOFScriptAspect(
        ArrayList<MOFScriptModel_Advice> mofscriptmodel_advices    ) {
        this.mofscriptmodel_advices = mofscriptmodel_advices;
    }


    public List<MOFScriptModel_Advice> getMofscriptmodel_advices() {
        return mofscriptmodel_advices;
    }

    public void addMofscriptmodel_advice(Mofscriptmodel_advice mofscriptmodel_advice) {
        this.mofscriptmodel_advices.add(mofscriptmodel_advice);
    }

}