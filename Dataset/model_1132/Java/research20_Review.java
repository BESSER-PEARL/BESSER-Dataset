




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class research20_Review extends Labelled {

    private LocalDate date;





    private research20_ReviewNote research20_reviewnote;




    private research20_Researcher research20_researcher;


    public research20_Review(
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

    public research20_ReviewNote getResearch20_reviewnote() {
        return research20_reviewnote;
    }

    public void setResearch20_reviewnote(research20_ReviewNote research20_reviewnote) {
        this.research20_reviewnote = research20_reviewnote;
    }
    public research20_Researcher getResearch20_researcher() {
        return research20_researcher;
    }

    public void setResearch20_researcher(research20_Researcher research20_researcher) {
        this.research20_researcher = research20_researcher;
    }

}