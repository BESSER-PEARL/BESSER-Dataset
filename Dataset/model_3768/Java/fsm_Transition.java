





import java.util.List;
import java.util.ArrayList;

public class fsm_Transition  {

    private String als;
    private String ls;



    public fsm_Transition(
        String als,        String ls    ) {
        this.als = als;
        this.ls = ls;
    }


    public String getAls() {
        return als;
    }

    public void setAls(String als) {
        this.als = als;
    }
    public String getLs() {
        return ls;
    }

    public void setLs(String ls) {
        this.ls = ls;
    }


}