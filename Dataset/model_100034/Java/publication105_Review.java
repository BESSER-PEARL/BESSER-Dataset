




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class publication105_Review extends Labelled {

    private LocalDate date;





    private publication105_Researcher publication105_researcher;


    public publication105_Review(
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

    public publication105_Researcher getPublication105_researcher() {
        return publication105_researcher;
    }

    public void setPublication105_researcher(publication105_Researcher publication105_researcher) {
        this.publication105_researcher = publication105_researcher;
    }

}