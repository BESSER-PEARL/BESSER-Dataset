




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class itm_Version  {

    private String name;
    private LocalDate completedDate;
    private String description;
    private String status;





    private itm_Project itm_project;


    public itm_Version(
        String name,        LocalDate completedDate,        String description,        String status    ) {
        this.name = name;
        this.completedDate = completedDate;
        this.description = description;
        this.status = status;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public LocalDate getCompleteddate() {
        return completedDate;
    }

    public void setCompleteddate(LocalDate completedDate) {
        this.completedDate = completedDate;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }

    public itm_Project getItm_project() {
        return itm_project;
    }

    public void setItm_project(itm_Project itm_project) {
        this.itm_project = itm_project;
    }

}