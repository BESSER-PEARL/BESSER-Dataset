





import java.util.List;
import java.util.ArrayList;

public class ocl_cst_OperationCallExpCS extends FeatureCallExpCS {

    private String isAtomic;



    public ocl_cst_OperationCallExpCS(
        String isAtomic    ) {
        super(
        );
        this.isAtomic = isAtomic;
    }


    public String getIsatomic() {
        return isAtomic;
    }

    public void setIsatomic(String isAtomic) {
        this.isAtomic = isAtomic;
    }


}