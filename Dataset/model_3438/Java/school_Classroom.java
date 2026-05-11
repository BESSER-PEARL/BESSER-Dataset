





import java.util.List;
import java.util.ArrayList;

public class school_Classroom  {

    private int capacity;
    private String teacher;
    private String name;
    private int rank;



    public school_Classroom(
        int capacity,        String teacher,        String name,        int rank    ) {
        this.capacity = capacity;
        this.teacher = teacher;
        this.name = name;
        this.rank = rank;
    }


    public int getCapacity() {
        return capacity;
    }

    public void setCapacity(int capacity) {
        this.capacity = capacity;
    }
    public String getTeacher() {
        return teacher;
    }

    public void setTeacher(String teacher) {
        this.teacher = teacher;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getRank() {
        return rank;
    }

    public void setRank(int rank) {
        this.rank = rank;
    }


}