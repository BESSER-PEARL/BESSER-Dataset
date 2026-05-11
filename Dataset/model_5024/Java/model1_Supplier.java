





import java.util.List;
import java.util.ArrayList;

public class model1_Supplier extends Address {

    private boolean preferred;



    public model1_Supplier(
        boolean preferred    ) {
        super(
        );
        this.preferred = preferred;
    }


    public boolean getPreferred() {
        return preferred;
    }

    public void setPreferred(boolean preferred) {
        this.preferred = preferred;
    }


}