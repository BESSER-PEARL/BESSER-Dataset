




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class researchvc_Review extends Labelled {

    private LocalDate date;





    private researchvc_Researcher researchvc_researcher;


    public researchvc_Review(
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

    public researchvc_Researcher getResearchvc_researcher() {
        return researchvc_researcher;
    }

    public void setResearchvc_researcher(researchvc_Researcher researchvc_researcher) {
        this.researchvc_researcher = researchvc_researcher;
    }

}