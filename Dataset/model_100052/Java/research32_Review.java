




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class research32_Review extends Labelled {

    private LocalDate date;





    private research32_Researcher research32_researcher;




    private research32_ReviewNote research32_reviewnote;


    public research32_Review(
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

    public research32_Researcher getResearch32_researcher() {
        return research32_researcher;
    }

    public void setResearch32_researcher(research32_Researcher research32_researcher) {
        this.research32_researcher = research32_researcher;
    }
    public research32_ReviewNote getResearch32_reviewnote() {
        return research32_reviewnote;
    }

    public void setResearch32_reviewnote(research32_ReviewNote research32_reviewnote) {
        this.research32_reviewnote = research32_reviewnote;
    }

}