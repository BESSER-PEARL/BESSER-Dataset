





import java.util.List;
import java.util.ArrayList;

public class HALL_FSMActions_MessageInvocation extends ActionExpressionElement {

    private boolean isTopDown;
    private String name;



    public HALL_FSMActions_MessageInvocation(
        boolean isTopDown,        String name    ) {
        super(
        );
        this.isTopDown = isTopDown;
        this.name = name;
    }


    public boolean getIstopdown() {
        return isTopDown;
    }

    public void setIstopdown(boolean isTopDown) {
        this.isTopDown = isTopDown;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}