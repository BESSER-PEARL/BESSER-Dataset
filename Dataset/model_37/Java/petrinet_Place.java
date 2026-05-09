





import java.util.List;
import java.util.ArrayList;

public class petrinet_Place extends Node {

    private int capacity;
    private int tokens;



    public petrinet_Place(
        int capacity,        int tokens    ) {
        super(
        );
        this.capacity = capacity;
        this.tokens = tokens;
    }


    public int getCapacity() {
        return capacity;
    }

    public void setCapacity(int capacity) {
        this.capacity = capacity;
    }
    public int getTokens() {
        return tokens;
    }

    public void setTokens(int tokens) {
        this.tokens = tokens;
    }


}