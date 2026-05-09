




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class publication101_Review extends Labelled {

    private LocalDate date;





    private publication101_Researcher publication101_researcher;




    private publication101_ReviewNote publication101_reviewnote;


    public publication101_Review(
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

    public publication101_Researcher getPublication101_researcher() {
        return publication101_researcher;
    }

    public void setPublication101_researcher(publication101_Researcher publication101_researcher) {
        this.publication101_researcher = publication101_researcher;
    }
    public publication101_ReviewNote getPublication101_reviewnote() {
        return publication101_reviewnote;
    }

    public void setPublication101_reviewnote(publication101_ReviewNote publication101_reviewnote) {
        this.publication101_reviewnote = publication101_reviewnote;
    }

}