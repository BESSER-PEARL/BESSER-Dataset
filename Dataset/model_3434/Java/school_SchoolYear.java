




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class school_SchoolYear  {

    private LocalDate year;





    private List<school_ClassGroup> school_classgroups;




    private List<school_ClassLevel> school_classlevels;




    private List<school_Student> school_students;


    public school_SchoolYear(
        LocalDate year    ) {
        this.year = year;
        this.school_classgroups = new ArrayList<>();
        this.school_classlevels = new ArrayList<>();
        this.school_students = new ArrayList<>();
    }

    public school_SchoolYear(
        LocalDate year        ArrayList<school_ClassGroup> school_classgroups,        ArrayList<school_ClassLevel> school_classlevels,        ArrayList<school_Student> school_students    ) {
        this.year = year;
        this.school_classgroups = school_classgroups;
        this.school_classlevels = school_classlevels;
        this.school_students = school_students;
    }

    public LocalDate getYear() {
        return year;
    }

    public void setYear(LocalDate year) {
        this.year = year;
    }

    public List<school_ClassGroup> getSchool_classgroups() {
        return school_classgroups;
    }

    public void addSchool_classgroup(School_classgroup school_classgroup) {
        this.school_classgroups.add(school_classgroup);
    }
    public List<school_ClassLevel> getSchool_classlevels() {
        return school_classlevels;
    }

    public void addSchool_classlevel(School_classlevel school_classlevel) {
        this.school_classlevels.add(school_classlevel);
    }
    public List<school_Student> getSchool_students() {
        return school_students;
    }

    public void addSchool_student(School_student school_student) {
        this.school_students.add(school_student);
    }

}