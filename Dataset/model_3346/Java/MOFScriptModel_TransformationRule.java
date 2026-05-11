





import java.util.List;
import java.util.ArrayList;

public class MOFScriptModel_TransformationRule extends MOFScriptStatementOwner {

    private boolean isEntryPoint;
    private String return_;
    private String name;
    private String accessLevel;
    private boolean isAbstract;





    private MOFScriptModel_TransformationRule mofscriptmodel_transformationrule;


    public MOFScriptModel_TransformationRule(
        boolean isEntryPoint,        String return_,        String name,        String accessLevel,        boolean isAbstract    ) {
        super(
        );
        this.isEntryPoint = isEntryPoint;
        this.return_ = return_;
        this.name = name;
        this.accessLevel = accessLevel;
        this.isAbstract = isAbstract;
    }


    public boolean getIsentrypoint() {
        return isEntryPoint;
    }

    public void setIsentrypoint(boolean isEntryPoint) {
        this.isEntryPoint = isEntryPoint;
    }
    public String getReturn_() {
        return return_;
    }

    public void setReturn_(String return_) {
        this.return_ = return_;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getAccesslevel() {
        return accessLevel;
    }

    public void setAccesslevel(String accessLevel) {
        this.accessLevel = accessLevel;
    }
    public boolean getIsabstract() {
        return isAbstract;
    }

    public void setIsabstract(boolean isAbstract) {
        this.isAbstract = isAbstract;
    }

    public MOFScriptModel_TransformationRule getMofscriptmodel_transformationrule() {
        return mofscriptmodel_transformationrule;
    }

    public void setMofscriptmodel_transformationrule(MOFScriptModel_TransformationRule mofscriptmodel_transformationrule) {
        this.mofscriptmodel_transformationrule = mofscriptmodel_transformationrule;
    }

}