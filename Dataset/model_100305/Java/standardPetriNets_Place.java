





import java.util.List;
import java.util.ArrayList;

public class standardPetriNets_Place  {

    private int capacity;
    private String name;
    private int numOfTokens;



    public standardPetriNets_Place(
        int capacity,        String name,        int numOfTokens    ) {
        this.capacity = capacity;
        this.name = name;
        this.numOfTokens = numOfTokens;
    }


    public int getCapacity() {
        return capacity;
    }

    public void setCapacity(int capacity) {
        this.capacity = capacity;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getNumoftokens() {
        return numOfTokens;
    }

    public void setNumoftokens(int numOfTokens) {
        this.numOfTokens = numOfTokens;
    }


}