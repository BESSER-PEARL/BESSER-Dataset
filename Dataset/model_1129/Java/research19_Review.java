




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class research19_Review extends Labelled {

    private LocalDate date;





    private research19_Researcher research19_researcher;


    public research19_Review(
        LocalDate date    ) {
        super(
        );
        this.date = date;
    }


    public LocalDate getDate() {
        return date;
    }

    public void setDate(LocalDate date) {
        this.date = date;
    }

    public research19_Researcher getResearch19_researcher() {
        return research19_researcher;
    }

    public void setResearch19_researcher(research19_Researcher research19_researcher) {
        this.research19_researcher = research19_researcher;
    }

}