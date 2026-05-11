





import java.util.List;
import java.util.ArrayList;

public class eol_types_ModelElementType extends AnyType {

    private String modelName;
    private String elementName;



    public eol_types_ModelElementType(
        String modelName,        String elementName    ) {
        super(
        );
        this.modelName = modelName;
        this.elementName = elementName;
    }


    public String getModelname() {
        return modelName;
    }

    public void setModelname(String modelName) {
        this.modelName = modelName;
    }
    public String getElementname() {
        return elementName;
    }

    public void setElementname(String elementName) {
        this.elementName = elementName;
    }


}