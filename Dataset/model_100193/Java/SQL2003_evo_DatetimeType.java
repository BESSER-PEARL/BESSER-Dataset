





import java.util.List;
import java.util.ArrayList;

public class SQL2003_evo_DatetimeType extends PredefinedType {

    private String descriptor;



    public SQL2003_evo_DatetimeType(
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