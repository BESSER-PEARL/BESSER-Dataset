





import java.util.List;
import java.util.ArrayList;

public class Employee  {

    private int Mid;
    private int Eid;



    public Employee(
        int Mid,        int Eid    ) {
        this.Mid = Mid;
        this.Eid = Eid;
    }


    public int getMid() {
        return Mid;
    }

    public void setMid(int Mid) {
        this.Mid = Mid;
    }
    public int getEid() {
        return Eid;
    }

    public void setEid(int Eid) {
        this.Eid = Eid;
    }


}