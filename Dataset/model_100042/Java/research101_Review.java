




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class research101_Review extends Labelled {

    private LocalDate date;





    private research101_ReviewNote research101_reviewnote;




    private research101_Researcher research101_researcher;


    public research101_Review(
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

    public research101_ReviewNote getResearch101_reviewnote() {
        return research101_reviewnote;
    }

    public void setResearch101_reviewnote(research101_ReviewNote research101_reviewnote) {
        this.research101_reviewnote = research101_reviewnote;
    }
    public research101_Researcher getResearch101_researcher() {
        return research101_researcher;
    }

    public void setResearch101_researcher(research101_Researcher research101_researcher) {
        this.research101_researcher = research101_researcher;
    }

}