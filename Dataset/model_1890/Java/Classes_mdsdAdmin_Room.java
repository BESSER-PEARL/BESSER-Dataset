





import java.util.List;
import java.util.ArrayList;

public class Classes_mdsdAdmin_Room  {

    private String type;
    private int number;
    private String status;



    public Classes_mdsdAdmin_Room(
        String type,        int number,        String status    ) {
        this.type = type;
        this.number = number;
        this.status = status;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public int getNumber() {
        return number;
    }

    public void setNumber(int number) {
        this.number = number;
    }
    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }


}