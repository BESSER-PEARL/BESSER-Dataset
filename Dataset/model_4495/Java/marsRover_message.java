





import java.util.List;
import java.util.ArrayList;

public class marsRover_message  {

    private String msg;
    private String name;



    public marsRover_message(
        String msg,        String name    ) {
        this.msg = msg;
        this.name = name;
    }


    public String getMsg() {
        return msg;
    }

    public void setMsg(String msg) {
        this.msg = msg;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}