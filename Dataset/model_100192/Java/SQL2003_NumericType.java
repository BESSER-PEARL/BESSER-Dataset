





import java.util.List;
import java.util.ArrayList;

public class SQL2003_NumericType extends PredefinedType {

    private String descriptor;



    public SQL2003_NumericType(
        String descriptor    ) {
        super(
        );
        this.descriptor = descriptor;
    }


    public String getDescriptor() {
        return descriptor;
    }

    public void setDescriptor(String descriptor) {
        this.descriptor = descriptor;
    }


}