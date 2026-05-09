





import java.util.List;
import java.util.ArrayList;

public class pivot_OperationCallExp extends ReferringElement, FeatureCallExp {

    private String isVirtual;



    public pivot_OperationCallExp(
        String isVirtual    ) {
        super(
        );
        this.isVirtual = isVirtual;
    }


    public String getIsvirtual() {
        return isVirtual;
    }

    public void setIsvirtual(String isVirtual) {
        this.isVirtual = isVirtual;
    }


}