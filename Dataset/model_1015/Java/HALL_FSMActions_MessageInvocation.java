





import java.util.List;
import java.util.ArrayList;

public class HALL_FSMActions_MessageInvocation extends ActionExpressionElement {

    private String name;
    private boolean isTopDown;



    public HALL_FSMActions_MessageInvocation(
        String name,        boolean isTopDown    ) {
        super(
        );
        this.name = name;
        this.isTopDown = isTopDown;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getIstopdown() {
        return isTopDown;
    }

    public void setIstopdown(boolean isTopDown) {
        this.isTopDown = isTopDown;
    }


}