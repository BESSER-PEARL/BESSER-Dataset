





import java.util.List;
import java.util.ArrayList;

public class notation_DrawerStyle extends Style {

    private boolean collapsed;



    public notation_DrawerStyle(
        boolean collapsed    ) {
        super(
        );
        this.collapsed = collapsed;
    }


    public boolean getCollapsed() {
        return collapsed;
    }

    public void setCollapsed(boolean collapsed) {
        this.collapsed = collapsed;
    }


}