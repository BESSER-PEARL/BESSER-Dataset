





import java.util.List;
import java.util.ArrayList;

public class fml_List extends DisplayElement {

    private boolean isOrdered;



    public fml_List(
        boolean isOrdered    ) {
        super(
        );
        this.isOrdered = isOrdered;
    }


    public boolean getIsordered() {
        return isOrdered;
    }

    public void setIsordered(boolean isOrdered) {
        this.isOrdered = isOrdered;
    }


}