




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class gore_DefinableRequirement extends Requirement {

    private String state;
    private LocalDate time;



    public gore_DefinableRequirement(
        String state,        LocalDate time    ) {
        super(
        );
        this.state = state;
        this.time = time;
    }


    public String getState() {
        return state;
    }

    public void setState(String state) {
        this.state = state;
    }
    public LocalDate getTime() {
        return time;
    }

    public void setTime(LocalDate time) {
        this.time = time;
    }


}