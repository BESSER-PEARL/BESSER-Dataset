





import java.util.List;
import java.util.ArrayList;

public class statespace_EqualityHelper  {

    private boolean checkLinkOrder;





    private statespace_StateSpace statespace_statespace;


    public statespace_EqualityHelper(
        boolean checkLinkOrder    ) {
        this.checkLinkOrder = checkLinkOrder;
    }


    public boolean getChecklinkorder() {
        return checkLinkOrder;
    }

    public void setChecklinkorder(boolean checkLinkOrder) {
        this.checkLinkOrder = checkLinkOrder;
    }

    public statespace_StateSpace getStatespace_statespace() {
        return statespace_statespace;
    }

    public void setStatespace_statespace(statespace_StateSpace statespace_statespace) {
        this.statespace_statespace = statespace_statespace;
    }

}