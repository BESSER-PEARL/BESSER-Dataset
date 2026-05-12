




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class gore_PerformativeRequirement extends DefinableRequirement {

    private LocalDate startTime;



    public gore_PerformativeRequirement(
        LocalDate startTime    ) {
        super(
        );
        this.startTime = startTime;
    }


    public LocalDate getStarttime() {
        return startTime;
    }

    public void setStarttime(LocalDate startTime) {
        this.startTime = startTime;
    }


}