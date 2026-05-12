





import java.util.List;
import java.util.ArrayList;

public class Login_Process  {

    private String Time_Out;
    private String Time_In;



    public Login_Process(
        String Time_Out,        String Time_In    ) {
        this.Time_Out = Time_Out;
        this.Time_In = Time_In;
    }


    public String getTime_out() {
        return Time_Out;
    }

    public void setTime_out(String Time_Out) {
        this.Time_Out = Time_Out;
    }
    public String getTime_in() {
        return Time_In;
    }

    public void setTime_in(String Time_In) {
        this.Time_In = Time_In;
    }


}