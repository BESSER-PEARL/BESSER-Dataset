




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class publication103_Review extends Labelled {

    private LocalDate date;





    private publication103_Researcher publication103_researcher;




    private publication103_ReviewNote publication103_reviewnote;


    public publication103_Review(
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

    public publication103_Researcher getPublication103_researcher() {
        return publication103_researcher;
    }

    public void setPublication103_researcher(publication103_Researcher publication103_researcher) {
        this.publication103_researcher = publication103_researcher;
    }
    public publication103_ReviewNote getPublication103_reviewnote() {
        return publication103_reviewnote;
    }

    public void setPublication103_reviewnote(publication103_ReviewNote publication103_reviewnote) {
        this.publication103_reviewnote = publication103_reviewnote;
    }

}