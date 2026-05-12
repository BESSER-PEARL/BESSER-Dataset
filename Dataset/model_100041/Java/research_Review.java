




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class research_Review extends Labelled {

    private LocalDate date;





    private research_Researcher research_researcher;


    public research_Review(
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

    public research_Researcher getResearch_researcher() {
        return research_researcher;
    }

    public void setResearch_researcher(research_Researcher research_researcher) {
        this.research_researcher = research_researcher;
    }

}