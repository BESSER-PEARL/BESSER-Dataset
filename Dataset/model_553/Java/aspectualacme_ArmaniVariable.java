





import java.util.List;
import java.util.ArrayList;

public class aspectualacme_ArmaniVariable extends ArmaniExpression {

    private String basicType;
    private String id;





    private aspectualacme_TypeDefinition aspectualacme_typedefinition;


    public aspectualacme_ArmaniVariable(
        String basicType,        String id    ) {
        super(
        );
        this.basicType = basicType;
        this.id = id;
    }


    public String getBasictype() {
        return basicType;
    }

    public void setBasictype(String basicType) {
        this.basicType = basicType;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public aspectualacme_TypeDefinition getAspectualacme_typedefinition() {
        return aspectualacme_typedefinition;
    }

    public void setAspectualacme_typedefinition(aspectualacme_TypeDefinition aspectualacme_typedefinition) {
        this.aspectualacme_typedefinition = aspectualacme_typedefinition;
    }

}