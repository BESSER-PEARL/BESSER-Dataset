




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class model_task_WorkPackage extends WorkItem {

    private LocalDate startDate;
    private LocalDate endDate;



    public model_task_WorkPackage(
        LocalDate startDate,        LocalDate endDate    ) {
        super(
        );
        this.startDate = startDate;
        this.endDate = endDate;
    }


    public LocalDate getStartdate() {
        return startDate;
    }

    public void setStartdate(LocalDate startDate) {
        this.startDate = startDate;
    }
    public LocalDate getEnddate() {
        return endDate;
    }

    public void setEnddate(LocalDate endDate) {
        this.endDate = endDate;
    }


}