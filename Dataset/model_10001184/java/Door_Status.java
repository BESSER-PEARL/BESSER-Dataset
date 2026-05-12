





import java.util.List;
import java.util.ArrayList;

public class Door_Status  {

    private boolean Door_Open;
    private String Door_Close;



    public Door_Status(
        boolean Door_Open,        String Door_Close    ) {
        this.Door_Open = Door_Open;
        this.Door_Close = Door_Close;
    }


    public boolean getDoor_open() {
        return Door_Open;
    }

    public void setDoor_open(boolean Door_Open) {
        this.Door_Open = Door_Open;
    }
    public String getDoor_close() {
        return Door_Close;
    }

    public void setDoor_close(String Door_Close) {
        this.Door_Close = Door_Close;
    }


}