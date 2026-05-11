





import java.util.List;
import java.util.ArrayList;

public class model_types_JvmPrimitiveType extends JvmComponentType {

    private String simpleName;



    public model_types_JvmPrimitiveType(
        String simpleName    ) {
        super(
        );
        this.simpleName = simpleName;
    }


    public String getSimplename() {
        return simpleName;
    }

    public void setSimplename(String simpleName) {
        this.simpleName = simpleName;
    }


}