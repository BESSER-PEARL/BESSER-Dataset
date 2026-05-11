





import java.util.List;
import java.util.ArrayList;

public class titan_MultiDataType extends DataType {

    private boolean unique;



    public titan_MultiDataType(
        boolean unique    ) {
        super(
        );
        this.unique = unique;
    }


    public boolean getUnique() {
        return unique;
    }

    public void setUnique(boolean unique) {
        this.unique = unique;
    }


}