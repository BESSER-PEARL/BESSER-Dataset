





import java.util.List;
import java.util.ArrayList;

public class modelDsl_DefModelTypeVariable extends DefAttribute, DefIdAttribute {

    private String nullable;
    private String name;





    private modelDsl_ModelType modeldsl_modeltype;


    public modelDsl_DefModelTypeVariable(
        String nullable,        String name    ) {
        super(
        );
        this.nullable = nullable;
        this.name = name;
    }


    public String getNullable() {
        return nullable;
    }

    public void setNullable(String nullable) {
        this.nullable = nullable;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public modelDsl_ModelType getModeldsl_modeltype() {
        return modeldsl_modeltype;
    }

    public void setModeldsl_modeltype(modelDsl_ModelType modeldsl_modeltype) {
        this.modeldsl_modeltype = modeldsl_modeltype;
    }

}