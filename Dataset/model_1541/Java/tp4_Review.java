




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class tp4_Review extends Labelled {

    private LocalDate date;





    private tp4_ReviewNote tp4_reviewnote;




    private tp4_Researcher tp4_researcher;


    public tp4_Review(
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

    public tp4_ReviewNote getTp4_reviewnote() {
        return tp4_reviewnote;
    }

    public void setTp4_reviewnote(tp4_ReviewNote tp4_reviewnote) {
        this.tp4_reviewnote = tp4_reviewnote;
    }
    public tp4_Researcher getTp4_researcher() {
        return tp4_researcher;
    }

    public void setTp4_researcher(tp4_Researcher tp4_researcher) {
        this.tp4_researcher = tp4_researcher;
    }

}