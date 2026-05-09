





import java.util.List;
import java.util.ArrayList;

public class uma_SimpleSemanticModelElement extends SemanticModelBridge {

    private String typeInfo;



    public uma_SimpleSemanticModelElement(
        String typeInfo    ) {
        super(
        );
        this.typeInfo = typeInfo;
    }


    public String getTypeinfo() {
        return typeInfo;
    }

    public void setTypeinfo(String typeInfo) {
        this.typeInfo = typeInfo;
    }


}