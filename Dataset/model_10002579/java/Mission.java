




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Mission  {

    private int mission_NoOfDays;
    private LocalDate mission_StartDate;
    private String mission_Title;
    private String mission_Status;
    private int staff_Id;
    private LocalDate mission_EndDate;
    private int mission_id;
    private String mission_detail;





    private staff_member staff_member;


    public Mission(
        int mission_NoOfDays,        LocalDate mission_StartDate,        String mission_Title,        String mission_Status,        int staff_Id,        LocalDate mission_EndDate,        int mission_id,        String mission_detail    ) {
        this.mission_NoOfDays = mission_NoOfDays;
        this.mission_StartDate = mission_StartDate;
        this.mission_Title = mission_Title;
        this.mission_Status = mission_Status;
        this.staff_Id = staff_Id;
        this.mission_EndDate = mission_EndDate;
        this.mission_id = mission_id;
        this.mission_detail = mission_detail;
    }


    public int getMission_noofdays() {
        return mission_NoOfDays;
    }

    public void setMission_noofdays(int mission_NoOfDays) {
        this.mission_NoOfDays = mission_NoOfDays;
    }
    public LocalDate getMission_startdate() {
        return mission_StartDate;
    }

    public void setMission_startdate(LocalDate mission_StartDate) {
        this.mission_StartDate = mission_StartDate;
    }
    public String getMission_title() {
        return mission_Title;
    }

    public void setMission_title(String mission_Title) {
        this.mission_Title = mission_Title;
    }
    public String getMission_status() {
        return mission_Status;
    }

    public void setMission_status(String mission_Status) {
        this.mission_Status = mission_Status;
    }
    public int getStaff_id() {
        return staff_Id;
    }

    public void setStaff_id(int staff_Id) {
        this.staff_Id = staff_Id;
    }
    public LocalDate getMission_enddate() {
        return mission_EndDate;
    }

    public void setMission_enddate(LocalDate mission_EndDate) {
        this.mission_EndDate = mission_EndDate;
    }
    public int getMission_id() {
        return mission_id;
    }

    public void setMission_id(int mission_id) {
        this.mission_id = mission_id;
    }
    public String getMission_detail() {
        return mission_detail;
    }

    public void setMission_detail(String mission_detail) {
        this.mission_detail = mission_detail;
    }

    public staff_member getStaff_member() {
        return staff_member;
    }

    public void setStaff_member(staff_member staff_member) {
        this.staff_member = staff_member;
    }

}