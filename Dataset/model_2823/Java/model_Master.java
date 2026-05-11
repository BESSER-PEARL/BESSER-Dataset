





import java.util.List;
import java.util.ArrayList;

public class model_Master extends Widget, LinkSupport {

    private boolean dimmed;



    public model_Master(
        boolean dimmed    ) {
        super(
        );
        this.dimmed = dimmed;
    }


    public boolean getDimmed() {
        return dimmed;
    }

    public void setDimmed(boolean dimmed) {
        this.dimmed = dimmed;
    }


}