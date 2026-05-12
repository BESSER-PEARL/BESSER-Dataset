





import java.util.List;
import java.util.ArrayList;

public class Player  {

    private int bid;
    private int stack;



    public Player(
        int bid,        int stack    ) {
        this.bid = bid;
        this.stack = stack;
    }


    public int getBid() {
        return bid;
    }

    public void setBid(int bid) {
        this.bid = bid;
    }
    public int getStack() {
        return stack;
    }

    public void setStack(int stack) {
        this.stack = stack;
    }


}