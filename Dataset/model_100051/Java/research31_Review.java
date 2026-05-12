




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class research31_Review extends Labelled {

    private LocalDate date;





    private research31_Researcher research31_researcher;


    public research31_Review(
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

    public research31_Researcher getResearch31_researcher() {
        return research31_researcher;
    }

    public void setResearch31_researcher(research31_Researcher research31_researcher) {
        this.research31_researcher = research31_researcher;
    }

}