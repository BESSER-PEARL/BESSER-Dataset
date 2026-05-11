





import java.util.List;
import java.util.ArrayList;

public class MOFScriptModel_PointCut  {

    private String typeMatch;
    private String name;





    private MOFScriptModel_MOFScriptAspect mofscriptmodel_mofscriptaspect;




    private MOFScriptModel_Advice mofscriptmodel_advice;




    private MOFScriptModel_PointCutExpression mofscriptmodel_pointcutexpression;


    public MOFScriptModel_PointCut(
        String typeMatch,        String name    ) {
        this.typeMatch = typeMatch;
        this.name = name;
    }


    public String getTypematch() {
        return typeMatch;
    }

    public void setTypematch(String typeMatch) {
        this.typeMatch = typeMatch;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public MOFScriptModel_MOFScriptAspect getMofscriptmodel_mofscriptaspect() {
        return mofscriptmodel_mofscriptaspect;
    }

    public void setMofscriptmodel_mofscriptaspect(MOFScriptModel_MOFScriptAspect mofscriptmodel_mofscriptaspect) {
        this.mofscriptmodel_mofscriptaspect = mofscriptmodel_mofscriptaspect;
    }
    public MOFScriptModel_Advice getMofscriptmodel_advice() {
        return mofscriptmodel_advice;
    }

    public void setMofscriptmodel_advice(MOFScriptModel_Advice mofscriptmodel_advice) {
        this.mofscriptmodel_advice = mofscriptmodel_advice;
    }
    public MOFScriptModel_PointCutExpression getMofscriptmodel_pointcutexpression() {
        return mofscriptmodel_pointcutexpression;
    }

    public void setMofscriptmodel_pointcutexpression(MOFScriptModel_PointCutExpression mofscriptmodel_pointcutexpression) {
        this.mofscriptmodel_pointcutexpression = mofscriptmodel_pointcutexpression;
    }

}