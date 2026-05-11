




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class fopramodel_FoPra  {

    private String description;
    private LocalDate end;
    private LocalDate start;
    private String title;
    private int maxNumberOfStudents;
    private String status;



    public fopramodel_FoPra(
        String description,        LocalDate end,        LocalDate start,        String title,        int maxNumberOfStudents,        String status    ) {
        this.description = description;
        this.end = end;
        this.start = start;
        this.title = title;
        this.maxNumberOfStudents = maxNumberOfStudents;
        this.status = status;
    }


    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public LocalDate getEnd() {
        return end;
    }

    public void setEnd(LocalDate end) {
        this.end = end;
    }
    public LocalDate getStart() {
        return start;
    }

    public void setStart(LocalDate start) {
        this.start = start;
    }
    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }
    public int getMaxnumberofstudents() {
        return maxNumberOfStudents;
    }

    public void setMaxnumberofstudents(int maxNumberOfStudents) {
        this.maxNumberOfStudents = maxNumberOfStudents;
    }
    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }


}