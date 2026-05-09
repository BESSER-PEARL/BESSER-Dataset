




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class research23_Review extends Labelled {

    private LocalDate date;





    private research23_Researcher research23_researcher;




    private research23_ReviewNote research23_reviewnote;


    public research23_Review(
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

    public research23_Researcher getResearch23_researcher() {
        return research23_researcher;
    }

    public void setResearch23_researcher(research23_Researcher research23_researcher) {
        this.research23_researcher = research23_researcher;
    }
    public research23_ReviewNote getResearch23_reviewnote() {
        return research23_reviewnote;
    }

    public void setResearch23_reviewnote(research23_ReviewNote research23_reviewnote) {
        this.research23_reviewnote = research23_reviewnote;
    }

}