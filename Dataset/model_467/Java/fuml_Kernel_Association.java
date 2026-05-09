





import java.util.List;
import java.util.ArrayList;

public class fuml_Kernel_Association extends Classifier {

    private boolean derived;



    public fuml_Kernel_Association(
        boolean derived    ) {
        super(
        );
        this.derived = derived;
    }


    public boolean getDerived() {
        return derived;
    }

    public void setDerived(boolean derived) {
        this.derived = derived;
    }


}