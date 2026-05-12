





import java.util.List;
import java.util.ArrayList;

public class SQL2003_CharacterStringType extends PredefinedType {

    private String length_def;
    private String descriptor;



    public SQL2003_CharacterStringType(
        String length_def,        String descriptor    ) {
        super(
        );
        this.length_def = length_def;
        this.descriptor = descriptor;
    }


    public String getLength_def() {
        return length_def;
    }

    public void setLength_def(String length_def) {
        this.length_def = length_def;
    }
    public String getDescriptor() {
        return descriptor;
    }

    public void setDescriptor(String descriptor) {
        this.descriptor = descriptor;
    }


}