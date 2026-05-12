





import java.util.List;
import java.util.ArrayList;

public class Hashtag  {

    private int numOfRepeat;
    private String name;



    public Hashtag(
        int numOfRepeat,        String name    ) {
        this.numOfRepeat = numOfRepeat;
        this.name = name;
    }


    public int getNumofrepeat() {
        return numOfRepeat;
    }

    public void setNumofrepeat(int numOfRepeat) {
        this.numOfRepeat = numOfRepeat;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}