





import java.util.List;
import java.util.ArrayList;

public class mydsl_FSM  {

    private String name;





    private mydsl_Final mydsl_final;




    private mydsl_Initial mydsl_initial;


    public mydsl_FSM(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public mydsl_Final getMydsl_final() {
        return mydsl_final;
    }

    public void setMydsl_final(mydsl_Final mydsl_final) {
        this.mydsl_final = mydsl_final;
    }
    public mydsl_Initial getMydsl_initial() {
        return mydsl_initial;
    }

    public void setMydsl_initial(mydsl_Initial mydsl_initial) {
        this.mydsl_initial = mydsl_initial;
    }

}