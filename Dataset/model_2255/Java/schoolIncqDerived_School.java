





import java.util.List;
import java.util.ArrayList;

public class schoolIncqDerived_School  {

    private int currentYear;
    private String name;
    private String address;
    private int numberOfTeachers;



    public schoolIncqDerived_School(
        int currentYear,        String name,        String address,        int numberOfTeachers    ) {
        this.currentYear = currentYear;
        this.name = name;
        this.address = address;
        this.numberOfTeachers = numberOfTeachers;
    }


    public int getCurrentyear() {
        return currentYear;
    }

    public void setCurrentyear(int currentYear) {
        this.currentYear = currentYear;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }
    public int getNumberofteachers() {
        return numberOfTeachers;
    }

    public void setNumberofteachers(int numberOfTeachers) {
        this.numberOfTeachers = numberOfTeachers;
    }


}