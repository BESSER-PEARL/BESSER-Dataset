




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class research13_Review extends Labelled {

    private LocalDate date;





    private research13_Researcher research13_researcher;




    private research13_ReviewNote research13_reviewnote;


    public research13_Review(
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

    public research13_Researcher getResearch13_researcher() {
        return research13_researcher;
    }

    public void setResearch13_researcher(research13_Researcher research13_researcher) {
        this.research13_researcher = research13_researcher;
    }
    public research13_ReviewNote getResearch13_reviewnote() {
        return research13_reviewnote;
    }

    public void setResearch13_reviewnote(research13_ReviewNote research13_reviewnote) {
        this.research13_reviewnote = research13_reviewnote;
    }

}