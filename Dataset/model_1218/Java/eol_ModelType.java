





import java.util.List;
import java.util.ArrayList;

public class eol_ModelType extends AnyType {

    private String resolvedIMetamodel;
    private String modelName;



    public eol_ModelType(
        String resolvedIMetamodel,        String modelName    ) {
        super(
        );
        this.resolvedIMetamodel = resolvedIMetamodel;
        this.modelName = modelName;
    }


    public String getResolvedimetamodel() {
        return resolvedIMetamodel;
    }

    public void setResolvedimetamodel(String resolvedIMetamodel) {
        this.resolvedIMetamodel = resolvedIMetamodel;
    }
    public String getModelname() {
        return modelName;
    }

    public void setModelname(String modelName) {
        this.modelName = modelName;
    }


}