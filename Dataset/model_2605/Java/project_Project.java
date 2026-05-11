




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class project_Project  {

    private String longname;
    private String homepage;
    private LocalDate start;
    private String shortname;
    private LocalDate end;
    private String devmail;





    private project_Foundation project_foundation;




    private project_Project project_project;




    private project_Project project_project;


    public project_Project(
        String longname,        String homepage,        LocalDate start,        String shortname,        LocalDate end,        String devmail    ) {
        this.longname = longname;
        this.homepage = homepage;
        this.start = start;
        this.shortname = shortname;
        this.end = end;
        this.devmail = devmail;
    }


    public String getLongname() {
        return longname;
    }

    public void setLongname(String longname) {
        this.longname = longname;
    }
    public String getHomepage() {
        return homepage;
    }

    public void setHomepage(String homepage) {
        this.homepage = homepage;
    }
    public LocalDate getStart() {
        return start;
    }

    public void setStart(LocalDate start) {
        this.start = start;
    }
    public String getShortname() {
        return shortname;
    }

    public void setShortname(String shortname) {
        this.shortname = shortname;
    }
    public LocalDate getEnd() {
        return end;
    }

    public void setEnd(LocalDate end) {
        this.end = end;
    }
    public String getDevmail() {
        return devmail;
    }

    public void setDevmail(String devmail) {
        this.devmail = devmail;
    }

    public project_Foundation getProject_foundation() {
        return project_foundation;
    }

    public void setProject_foundation(project_Foundation project_foundation) {
        this.project_foundation = project_foundation;
    }
    public project_Project getProject_project() {
        return project_project;
    }

    public void setProject_project(project_Project project_project) {
        this.project_project = project_project;
    }
    public project_Project getProject_project() {
        return project_project;
    }

    public void setProject_project(project_Project project_project) {
        this.project_project = project_project;
    }

}