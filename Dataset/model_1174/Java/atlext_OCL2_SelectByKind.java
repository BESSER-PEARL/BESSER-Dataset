





import java.util.List;
import java.util.ArrayList;

public class atlext_OCL2_SelectByKind extends CollectionOperationCallExp {

    private boolean isExact;



    public atlext_OCL2_SelectByKind(
        boolean isExact    ) {
        super(
        );
        this.isExact = isExact;
    }


    public boolean getIsexact() {
        return isExact;
    }

    public void setIsexact(boolean isExact) {
        this.isExact = isExact;
    }


}