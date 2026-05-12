




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class researchva_Review extends Labelled {

    private LocalDate date;





    private researchva_Researcher researchva_researcher;


    public researchva_Review(
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

    public researchva_Researcher getResearchva_researcher() {
        return researchva_researcher;
    }

    public void setResearchva_researcher(researchva_Researcher researchva_researcher) {
        this.researchva_researcher = researchva_researcher;
    }

}