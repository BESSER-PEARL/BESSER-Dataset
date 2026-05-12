





import java.util.List;
import java.util.ArrayList;

public class SQL2003_V3_BinaryStringType extends PredefinedType {

    private String descriptor;
    private String length_def;



    public SQL2003_V3_BinaryStringType(
        String descriptor,        String length_def    ) {
        super(
        );
        this.descriptor = descriptor;
        this.length_def = length_def;
    }


    public String getDescriptor() {
        return descriptor;
    }

    public void setDescriptor(String descriptor) {
        this.descriptor = descriptor;
    }
    public String getLength_def() {
        return length_def;
    }

    public void setLength_def(String length_def) {
        this.length_def = length_def;
    }


}