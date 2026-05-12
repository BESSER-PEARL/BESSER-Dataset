




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class gore_DefinableRequirement extends Requirement {

    private LocalDate time;
    private String state;



    public gore_DefinableRequirement(
        LocalDate time,        String state    ) {
        super(
        );
        this.time = time;
        this.state = state;
    }


    public LocalDate getTime() {
        return time;
    }

    public void setTime(LocalDate time) {
        this.time = time;
    }
    public String getState() {
        return state;
    }

    public void setState(String state) {
        this.state = state;
    }


}