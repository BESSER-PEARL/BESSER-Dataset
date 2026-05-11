





import java.util.List;
import java.util.ArrayList;

public class MOFScriptModel_MOFScriptTransformation extends MOFScriptObject {

    private String name;
    private String extendsName;





    private MOFScriptModel_TransformationRule mofscriptmodel_transformationrule;




    private List<MOFScriptModel_TransformationRule> mofscriptmodel_transformationrules;




    private MOFScriptModel_MOFScriptTransformation mofscriptmodel_mofscripttransformation;


    public MOFScriptModel_MOFScriptTransformation(
        String name,        String extendsName    ) {
        super(
        );
        this.name = name;
        this.extendsName = extendsName;
        this.mofscriptmodel_transformationrules = new ArrayList<>();
    }

    public MOFScriptModel_MOFScriptTransformation(
        String name,        String extendsName        ArrayList<MOFScriptModel_TransformationRule> mofscriptmodel_transformationrules    ) {
        this.name = name;
        this.extendsName = extendsName;
        this.mofscriptmodel_transformationrules = mofscriptmodel_transformationrules;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getExtendsname() {
        return extendsName;
    }

    public void setExtendsname(String extendsName) {
        this.extendsName = extendsName;
    }

    public MOFScriptModel_TransformationRule getMofscriptmodel_transformationrule() {
        return mofscriptmodel_transformationrule;
    }

    public void setMofscriptmodel_transformationrule(MOFScriptModel_TransformationRule mofscriptmodel_transformationrule) {
        this.mofscriptmodel_transformationrule = mofscriptmodel_transformationrule;
    }
    public List<MOFScriptModel_TransformationRule> getMofscriptmodel_transformationrules() {
        return mofscriptmodel_transformationrules;
    }

    public void addMofscriptmodel_transformationrule(Mofscriptmodel_transformationrule mofscriptmodel_transformationrule) {
        this.mofscriptmodel_transformationrules.add(mofscriptmodel_transformationrule);
    }
    public MOFScriptModel_MOFScriptTransformation getMofscriptmodel_mofscripttransformation() {
        return mofscriptmodel_mofscripttransformation;
    }

    public void setMofscriptmodel_mofscripttransformation(MOFScriptModel_MOFScriptTransformation mofscriptmodel_mofscripttransformation) {
        this.mofscriptmodel_mofscripttransformation = mofscriptmodel_mofscripttransformation;
    }

}