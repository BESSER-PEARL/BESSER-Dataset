





import java.util.List;
import java.util.ArrayList;

public class eol_ModelType extends AnyType {

    private String modelName;
    private String resolvedIMetamodel;



    public eol_ModelType(
        String modelName,        String resolvedIMetamodel    ) {
        super(
        );
        this.modelName = modelName;
        this.resolvedIMetamodel = resolvedIMetamodel;
    }


    public String getModelname() {
        return modelName;
    }

    public void setModelname(String modelName) {
        this.modelName = modelName;
    }
    public String getResolvedimetamodel() {
        return resolvedIMetamodel;
    }

    public void setResolvedimetamodel(String resolvedIMetamodel) {
        this.resolvedIMetamodel = resolvedIMetamodel;
    }


}