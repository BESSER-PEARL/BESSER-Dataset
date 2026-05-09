




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class research16_Review extends Labelled {

    private LocalDate date;





    private research16_ReviewNote research16_reviewnote;




    private research16_Researcher research16_researcher;


    public research16_Review(
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

    public research16_ReviewNote getResearch16_reviewnote() {
        return research16_reviewnote;
    }

    public void setResearch16_reviewnote(research16_ReviewNote research16_reviewnote) {
        this.research16_reviewnote = research16_reviewnote;
    }
    public research16_Researcher getResearch16_researcher() {
        return research16_researcher;
    }

    public void setResearch16_researcher(research16_Researcher research16_researcher) {
        this.research16_researcher = research16_researcher;
    }

}