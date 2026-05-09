





import java.util.List;
import java.util.ArrayList;

public class HALL_Messages_MessageState  {

    private boolean isEnd;
    private boolean isActive;
    private boolean isContinue;
    private String name;



    public HALL_Messages_MessageState(
        boolean isEnd,        boolean isActive,        boolean isContinue,        String name    ) {
        this.isEnd = isEnd;
        this.isActive = isActive;
        this.isContinue = isContinue;
        this.name = name;
    }


    public boolean getIsend() {
        return isEnd;
    }

    public void setIsend(boolean isEnd) {
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
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}