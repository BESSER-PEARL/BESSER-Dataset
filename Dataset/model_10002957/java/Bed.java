





import java.util.List;
import java.util.ArrayList;

public class Bed  {

    private int num;





    private Ward ward;


    public Bed(
        int num    ) {
        this.num = num;
    }


    public int getNum() {
        return num;
    }

    public void setNum(int num) {
        this.num = num;
    }

    public Ward getWard() {
        return ward;
    }

    public void setWard(Ward ward) {
        this.ward = ward;
    }

}