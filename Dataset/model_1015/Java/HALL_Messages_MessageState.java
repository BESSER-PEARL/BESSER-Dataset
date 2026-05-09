





import java.util.List;
import java.util.ArrayList;

public class HALL_Messages_MessageState  {

    private boolean isActive;
    private boolean isContinue;
    private boolean isEnd;



    public HALL_Messages_MessageState(
        boolean isActive,        boolean isContinue,        boolean isEnd    ) {
        this.isActive = isActive;
        this.isContinue = isContinue;
        this.isEnd = isEnd;
    }


    public boolean getIsactive() {
        return isActive;
    }

    public void setIsactive(boolean isActive) {
        this.isActive = isActive;
    }
    public boolean getIscontinue() {
        return isContinue;
    }

    public void setIscontinue(boolean isContinue) {
        this.isContinue = isContinue;
    }
    public boolean getIsend() {
        return isEnd;
    }

    public void setIsend(boolean isEnd) {
        this.isEnd = isEnd;
    }


}