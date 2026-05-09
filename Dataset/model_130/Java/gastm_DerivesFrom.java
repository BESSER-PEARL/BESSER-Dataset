





import java.util.List;
import java.util.ArrayList;

public class gastm_DerivesFrom extends OtherSyntaxObject {

    private boolean isVirtual;



    public gastm_DerivesFrom(
        boolean isVirtual    ) {
        super(
        );
        this.isVirtual = isVirtual;
    }


    public boolean getIsvirtual() {
        return isVirtual;
    }

    public void setIsvirtual(boolean isVirtual) {
        this.isVirtual = isVirtual;
    }


}