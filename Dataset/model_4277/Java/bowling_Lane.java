





import java.util.List;
import java.util.ArrayList;

public class bowling_Lane  {

    private int number;





    private bowling_Alley bowling_alley;


    public bowling_Lane(
        int number    ) {
        this.number = number;
    }


    public int getNumber() {
        return number;
    }

    public void setNumber(int number) {
        this.number = number;
    }

    public bowling_Alley getBowling_alley() {
        return bowling_alley;
    }

    public void setBowling_alley(bowling_Alley bowling_alley) {
        this.bowling_alley = bowling_alley;
    }

}