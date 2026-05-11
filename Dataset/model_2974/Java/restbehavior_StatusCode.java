





import java.util.List;
import java.util.ArrayList;

public class restbehavior_StatusCode  {

    private int number;





    private restbehavior_ReturnAction restbehavior_returnaction;


    public restbehavior_StatusCode(
        int number    ) {
        this.number = number;
    }


    public int getNumber() {
        return number;
    }

    public void setNumber(int number) {
        this.number = number;
    }

    public restbehavior_ReturnAction getRestbehavior_returnaction() {
        return restbehavior_returnaction;
    }

    public void setRestbehavior_returnaction(restbehavior_ReturnAction restbehavior_returnaction) {
        this.restbehavior_returnaction = restbehavior_returnaction;
    }

}