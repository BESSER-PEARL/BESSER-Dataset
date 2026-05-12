





import java.util.List;
import java.util.ArrayList;

public class Course  {

    private None _4_Course;
    private None _2_Course;
    private None _3_Course;
    private None _1_Course;





    private Teachers teachers;




    private Students students;




    private Administrator administrator;




    private Department department;


    public Course(
        None _4_Course,        None _2_Course,        None _3_Course,        None _1_Course    ) {
        this._4_Course = _4_Course;
        this._2_Course = _2_Course;
        this._3_Course = _3_Course;
        this._1_Course = _1_Course;
    }


    public None get_4_course() {
        return _4_Course;
    }

    public void set_4_course(None _4_Course) {
        this._4_Course = _4_Course;
    }
    public None get_2_course() {
        return _2_Course;
    }

    public void set_2_course(None _2_Course) {
        this._2_Course = _2_Course;
    }
    public None get_3_course() {
        return _3_Course;
    }

    public void set_3_course(None _3_Course) {
        this._3_Course = _3_Course;
    }
    public None get_1_course() {
        return _1_Course;
    }

    public void set_1_course(None _1_Course) {
        this._1_Course = _1_Course;
    }

    public Teachers getTeachers() {
        return teachers;
    }

    public void setTeachers(Teachers teachers) {
        this.teachers = teachers;
    }
    public Students getStudents() {
        return students;
    }

    public void setStudents(Students students) {
        this.students = students;
    }
    public Administrator getAdministrator() {
        return administrator;
    }

    public void setAdministrator(Administrator administrator) {
        this.administrator = administrator;
    }
    public Department getDepartment() {
        return department;
    }

    public void setDepartment(Department department) {
        this.department = department;
    }

}