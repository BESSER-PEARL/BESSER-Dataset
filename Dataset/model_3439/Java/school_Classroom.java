





import java.util.List;
import java.util.ArrayList;

public class school_Classroom  {

    private int capacity;
    private int rank;
    private String name;
    private String teacher;



    public school_Classroom(
        int capacity,        int rank,        String name,        String teacher    ) {
        this.capacity = capacity;
        this.rank = rank;
        this.name = name;
        this.teacher = teacher;
    }


    public int getCapacity() {
        return capacity;
    }

    public void setCapacity(int capacity) {
        this.capacity = capacity;
    }
    public int getRank() {
        return rank;
    }

    public void setRank(int rank) {
        this.rank = rank;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getTeacher() {
        return teacher;
    }

    public void setTeacher(String teacher) {
        this.teacher = teacher;
    }


}