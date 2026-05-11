





import java.util.List;
import java.util.ArrayList;

public class types_JvmPrimitiveType extends JvmComponentType {

    private String simpleName;



    public types_JvmPrimitiveType(
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