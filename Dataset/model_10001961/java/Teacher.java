





import java.util.List;
import java.util.ArrayList;

public class Teacher  {

    private String teacher_name;
    private int phone;
    private int teacher_ID;
    private String class_list;



    public Teacher(
        String teacher_name,        int phone,        int teacher_ID,        String class_list    ) {
        this.teacher_name = teacher_name;
        this.phone = phone;
        this.teacher_ID = teacher_ID;
        this.class_list = class_list;
    }


    public String getTeacher_name() {
        return teacher_name;
    }

    public void setTeacher_name(String teacher_name) {
        this.teacher_name = teacher_name;
    }
    public int getPhone() {
        return phone;
    }

    public void setPhone(int phone) {
        this.phone = phone;
    }
    public int getTeacher_id() {
        return teacher_ID;
    }

    public void setTeacher_id(int teacher_ID) {
        this.teacher_ID = teacher_ID;
    }
    public String getClass_list() {
        return class_list;
    }

    public void setClass_list(String class_list) {
        this.class_list = class_list;
    }


}