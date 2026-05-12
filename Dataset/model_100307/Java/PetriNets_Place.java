





import java.util.List;
import java.util.ArrayList;

public class PetriNets_Place  {

    private String name;
    private int numberOfTokens;
    private int capacity;



    public PetriNets_Place(
        String name,        int numberOfTokens,        int capacity    ) {
        this.name = name;
        this.numberOfTokens = numberOfTokens;
        this.capacity = capacity;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getNumberoftokens() {
        return numberOfTokens;
    }

    public void setNumberoftokens(int numberOfTokens) {
        this.numberOfTokens = numberOfTokens;
    }
    public int getCapacity() {
        return capacity;
    }

    public void setCapacity(int capacity) {
        this.capacity = capacity;
    }


}