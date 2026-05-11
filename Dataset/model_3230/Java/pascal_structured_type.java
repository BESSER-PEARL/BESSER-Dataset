





import java.util.List;
import java.util.ArrayList;

public class pascal_structured_type  {

    private boolean packed;





    private pascal_type pascal_type;


    public pascal_structured_type(
        boolean packed    ) {
        this.packed = packed;
    }


    public boolean getPacked() {
        return packed;
    }

    public void setPacked(boolean packed) {
        this.packed = packed;
    }

    public pascal_type getPascal_type() {
        return pascal_type;
    }

    public void setPascal_type(pascal_type pascal_type) {
        this.pascal_type = pascal_type;
    }

}