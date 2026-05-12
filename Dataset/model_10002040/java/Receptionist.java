





import java.util.List;
import java.util.ArrayList;

public class Receptionist  {

    private String checkroom;
    private int no;



    public Receptionist(
        String checkroom,        int no    ) {
        this.checkroom = checkroom;
        this.no = no;
    }


    public String getCheckroom() {
        return checkroom;
    }

    public void setCheckroom(String checkroom) {
        this.checkroom = checkroom;
    }
    public int getNo() {
        return no;
    }

    public void setNo(int no) {
        this.no = no;
    }


}