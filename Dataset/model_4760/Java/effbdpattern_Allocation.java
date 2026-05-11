





import java.util.List;
import java.util.ArrayList;

public class effbdpattern_Allocation  {

    private String id;
    private boolean redundant;



    public effbdpattern_Allocation(
        String id,        boolean redundant    ) {
        this.id = id;
        this.redundant = redundant;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public boolean getRedundant() {
        return redundant;
    }

    public void setRedundant(boolean redundant) {
        this.redundant = redundant;
    }


}