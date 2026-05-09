




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class research18_Review extends Labelled {

    private LocalDate date;





    private research18_Researcher research18_researcher;




    private research18_ReviewNote research18_reviewnote;


    public research18_Review(
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

    public research18_Researcher getResearch18_researcher() {
        return research18_researcher;
    }

    public void setResearch18_researcher(research18_Researcher research18_researcher) {
        this.research18_researcher = research18_researcher;
    }
    public research18_ReviewNote getResearch18_reviewnote() {
        return research18_reviewnote;
    }

    public void setResearch18_reviewnote(research18_ReviewNote research18_reviewnote) {
        this.research18_reviewnote = research18_reviewnote;
    }

}