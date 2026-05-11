





import java.util.List;
import java.util.ArrayList;

public class MOFScriptModel_MOFScriptParameter extends MOFScriptObject {

    private String name;
    private String direction;
    private String typePrefix;
    private String type;





    private MOFScriptModel_TransformationRule mofscriptmodel_transformationrule;




    private MOFScriptModel_TransformationRule mofscriptmodel_transformationrule;




    private MOFScriptModel_MOFScriptTransformation mofscriptmodel_mofscripttransformation;


    public MOFScriptModel_MOFScriptParameter(
        String name,        String direction,        String typePrefix,        String type    ) {
        super(
        );
        this.name = name;
        this.direction = direction;
        this.typePrefix = typePrefix;
        this.type = type;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getDirection() {
        return direction;
    }

    public void setDirection(String direction) {
        this.direction = direction;
    }
    public String getTypeprefix() {
        return typePrefix;
    }

    public void setTypeprefix(String typePrefix) {
        this.typePrefix = typePrefix;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public MOFScriptModel_TransformationRule getMofscriptmodel_transformationrule() {
        return mofscriptmodel_transformationrule;
    }

    public void setMofscriptmodel_transformationrule(MOFScriptModel_TransformationRule mofscriptmodel_transformationrule) {
        this.mofscriptmodel_transformationrule = mofscriptmodel_transformationrule;
    }
    public MOFScriptModel_TransformationRule getMofscriptmodel_transformationrule() {
        return mofscriptmodel_transformationrule;
    }

    public void setMofscriptmodel_transformationrule(MOFScriptModel_TransformationRule mofscriptmodel_transformationrule) {
        this.mofscriptmodel_transformationrule = mofscriptmodel_transformationrule;
    }
    public MOFScriptModel_MOFScriptTransformation getMofscriptmodel_mofscripttransformation() {
        return mofscriptmodel_mofscripttransformation;
    }

    public void setMofscriptmodel_mofscripttransformation(MOFScriptModel_MOFScriptTransformation mofscriptmodel_mofscripttransformation) {
        this.mofscriptmodel_mofscripttransformation = mofscriptmodel_mofscripttransformation;
    }

}