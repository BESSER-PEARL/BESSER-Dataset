





import java.util.List;
import java.util.ArrayList;

public class myDsl_Vars  {

    private String v2;
    private String v1;





    private myDsl_Command mydsl_command;


    public myDsl_Vars(
        String v2,        String v1    ) {
        this.v2 = v2;
        this.v1 = v1;
    }


    public String getV2() {
        return v2;
    }

    public void setV2(String v2) {
        this.v2 = v2;
    }
    public String getV1() {
        return v1;
    }

    public void setV1(String v1) {
        this.v1 = v1;
    }

    public myDsl_Command getMydsl_command() {
        return mydsl_command;
    }

    public void setMydsl_command(myDsl_Command mydsl_command) {
        this.mydsl_command = mydsl_command;
    }

}