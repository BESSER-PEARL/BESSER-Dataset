





import java.util.List;
import java.util.ArrayList;

public class Computer  {

    private int compID;





    private Patron patron;


    public Computer(
        int compID    ) {
        this.compID = compID;
    }


    public int getCompid() {
        return compID;
    }

    public void setCompid(int compID) {
        this.compID = compID;
    }

    public Patron getPatron() {
        return patron;
    }

    public void setPatron(Patron patron) {
        this.patron = patron;
    }

}