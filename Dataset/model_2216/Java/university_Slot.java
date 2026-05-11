





import java.util.List;
import java.util.ArrayList;

public class university_Slot  {

    private int points;
    private String slotType;
    private String name;





    private university_ProgrammeSemesters university_programmesemesters;




    private university_ProgrammeSemesters university_programmesemesters;




    private List<university_CourseInstances> university_courseinstancess;


    public university_Slot(
        int points,        String slotType,        String name    ) {
        this.points = points;
        this.slotType = slotType;
        this.name = name;
        this.university_courseinstancess = new ArrayList<>();
    }

    public university_Slot(
        int points,        String slotType,        String name        ArrayList<university_CourseInstances> university_courseinstancess    ) {
        this.points = points;
        this.slotType = slotType;
        this.name = name;
        this.university_courseinstancess = university_courseinstancess;
    }

    public int getPoints() {
        return points;
    }

    public void setPoints(int points) {
        this.points = points;
    }
    public String getSlottype() {
        return slotType;
    }

    public void setSlottype(String slotType) {
        this.slotType = slotType;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public university_ProgrammeSemesters getUniversity_programmesemesters() {
        return university_programmesemesters;
    }

    public void setUniversity_programmesemesters(university_ProgrammeSemesters university_programmesemesters) {
        this.university_programmesemesters = university_programmesemesters;
    }
    public university_ProgrammeSemesters getUniversity_programmesemesters() {
        return university_programmesemesters;
    }

    public void setUniversity_programmesemesters(university_ProgrammeSemesters university_programmesemesters) {
        this.university_programmesemesters = university_programmesemesters;
    }
    public List<university_CourseInstances> getUniversity_courseinstancess() {
        return university_courseinstancess;
    }

    public void addUniversity_courseinstances(University_courseinstances university_courseinstances) {
        this.university_courseinstancess.add(university_courseinstances);
    }

}