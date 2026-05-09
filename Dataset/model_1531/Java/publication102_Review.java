




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class publication102_Review extends Labelled {

    private LocalDate date;





    private publication102_Researcher publication102_researcher;


    public publication102_Review(
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

    public publication102_Researcher getPublication102_researcher() {
        return publication102_researcher;
    }

    public void setPublication102_researcher(publication102_Researcher publication102_researcher) {
        this.publication102_researcher = publication102_researcher;
    }

}