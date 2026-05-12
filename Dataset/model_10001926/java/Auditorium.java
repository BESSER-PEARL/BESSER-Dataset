





import java.util.List;
import java.util.ArrayList;

public class Auditorium  {

    private boolean is_busy;
    private String educationalBuilding;
    private int auditoriumNumber;
    private int id;



    public Auditorium(
        boolean is_busy,        String educationalBuilding,        int auditoriumNumber,        int id    ) {
        this.is_busy = is_busy;
        this.educationalBuilding = educationalBuilding;
        this.auditoriumNumber = auditoriumNumber;
        this.id = id;
    }


    public boolean getIs_busy() {
        return is_busy;
    }

    public void setIs_busy(boolean is_busy) {
        this.is_busy = is_busy;
    }
    public String getEducationalbuilding() {
        return educationalBuilding;
    }

    public void setEducationalbuilding(String educationalBuilding) {
        this.educationalBuilding = educationalBuilding;
    }
    public int getAuditoriumnumber() {
        return auditoriumNumber;
    }

    public void setAuditoriumnumber(int auditoriumNumber) {
        this.auditoriumNumber = auditoriumNumber;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }


}