





import java.util.List;
import java.util.ArrayList;

public class types_JvmFormalParameter extends JvmAnnotationTarget {

    private String name;





    private types_JvmExecutable types_jvmexecutable;


    public types_JvmFormalParameter(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public types_JvmExecutable getTypes_jvmexecutable() {
        return types_jvmexecutable;
    }

    public void setTypes_jvmexecutable(types_JvmExecutable types_jvmexecutable) {
        this.types_jvmexecutable = types_jvmexecutable;
    }

}