





import java.util.List;
import java.util.ArrayList;

public class School  {

    private int teachersCount;
    private None fields;
    private int name;
    private None teachers;
    private int studentsCount;
    private int fieldsCount;
    private None students;
    private None headmaster;



    public School(
        int teachersCount,        None fields,        int name,        None teachers,        int studentsCount,        int fieldsCount,        None students,        None headmaster    ) {
        this.teachersCount = teachersCount;
        this.fields = fields;
        this.name = name;
        this.teachers = teachers;
        this.studentsCount = studentsCount;
        this.fieldsCount = fieldsCount;
        this.students = students;
        this.headmaster = headmaster;
    }


    public int getTeacherscount() {
        return teachersCount;
    }

    public void setTeacherscount(int teachersCount) {
        this.teachersCount = teachersCount;
    }
    public None getFields() {
        return fields;
    }

    public void setFields(None fields) {
        this.fields = fields;
    }
    public int getName() {
        return name;
    }

    public void setName(int name) {
        this.name = name;
    }
    public None getTeachers() {
        return teachers;
    }

    public void setTeachers(None teachers) {
        this.teachers = teachers;
    }
    public int getStudentscount() {
        return studentsCount;
    }

    public void setStudentscount(int studentsCount) {
        this.studentsCount = studentsCount;
    }
    public int getFieldscount() {
        return fieldsCount;
    }

    public void setFieldscount(int fieldsCount) {
        this.fieldsCount = fieldsCount;
    }
    public None getStudents() {
        return students;
    }

    public void setStudents(None students) {
        this.students = students;
    }
    public None getHeadmaster() {
        return headmaster;
    }

    public void setHeadmaster(None headmaster) {
        this.headmaster = headmaster;
    }


}