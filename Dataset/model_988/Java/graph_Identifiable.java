





import java.util.List;
import java.util.ArrayList;

public class graph_Identifiable  {

    private int number;
    private String ID;



    public graph_Identifiable(
        int number,        String ID    ) {
        this.number = number;
        this.ID = ID;
    }


    public int getNumber() {
        return number;
    }

    public void setNumber(int number) {
        this.number = number;
    }
    public String getId() {
        return ID;
    }

    public void setId(String ID) {
        this.ID = ID;
    }


}