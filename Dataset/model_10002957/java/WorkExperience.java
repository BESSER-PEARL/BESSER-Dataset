




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class WorkExperience  {

    private String organization_name;
    private LocalDate finish_date;
    private String position;
    private LocalDate start_date;



    public WorkExperience(
        String organization_name,        LocalDate finish_date,        String position,        LocalDate start_date    ) {
        this.organization_name = organization_name;
        this.finish_date = finish_date;
        this.position = position;
        this.start_date = start_date;
    }


    public String getOrganization_name() {
        return organization_name;
    }

    public void setOrganization_name(String organization_name) {
        this.organization_name = organization_name;
    }
    public LocalDate getFinish_date() {
        return finish_date;
    }

    public void setFinish_date(LocalDate finish_date) {
        this.finish_date = finish_date;
    }
    public String getPosition() {
        return position;
    }

    public void setPosition(String position) {
        this.position = position;
    }
    public LocalDate getStart_date() {
        return start_date;
    }

    public void setStart_date(LocalDate start_date) {
        this.start_date = start_date;
    }


}