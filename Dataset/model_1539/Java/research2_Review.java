




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class research2_Review extends Labelled {

    private LocalDate date;





    private research2_Researcher research2_researcher;




    private research2_ReviewNote research2_reviewnote;


    public research2_Review(
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

    public research2_Researcher getResearch2_researcher() {
        return research2_researcher;
    }

    public void setResearch2_researcher(research2_Researcher research2_researcher) {
        this.research2_researcher = research2_researcher;
    }
    public research2_ReviewNote getResearch2_reviewnote() {
        return research2_reviewnote;
    }

    public void setResearch2_reviewnote(research2_ReviewNote research2_reviewnote) {
        this.research2_reviewnote = research2_reviewnote;
    }

}