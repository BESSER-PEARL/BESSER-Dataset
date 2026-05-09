





import java.util.List;
import java.util.ArrayList;

public class petrinet_Place extends Node {

    private int tokens;
    private int capacity;



    public petrinet_Place(
        int tokens,        int capacity    ) {
        super(
        );
        this.tokens = tokens;
        this.capacity = capacity;
    }


    public int getTokens() {
        return tokens;
    }

    public void setTokens(int tokens) {
        this.tokens = tokens;
    }
    public int getCapacity() {
        return capacity;
    }

    public void setCapacity(int capacity) {
        this.capacity = capacity;
    }


}