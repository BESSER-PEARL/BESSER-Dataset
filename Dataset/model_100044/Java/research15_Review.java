




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class research15_Review extends Labelled {

    private LocalDate date;





    private research15_Researcher research15_researcher;




    private research15_ReviewNote research15_reviewnote;


    public research15_Review(
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

    public research15_Researcher getResearch15_researcher() {
        return research15_researcher;
    }

    public void setResearch15_researcher(research15_Researcher research15_researcher) {
        this.research15_researcher = research15_researcher;
    }
    public research15_ReviewNote getResearch15_reviewnote() {
        return research15_reviewnote;
    }

    public void setResearch15_reviewnote(research15_ReviewNote research15_reviewnote) {
        this.research15_reviewnote = research15_reviewnote;
    }

}