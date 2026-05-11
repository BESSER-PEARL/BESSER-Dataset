





import java.util.List;
import java.util.ArrayList;

public class classmate_School  {

    private String name;





    private classmate_ClassmateSystem classmate_classmatesystem;


    public classmate_School(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public classmate_ClassmateSystem getClassmate_classmatesystem() {
        return classmate_classmatesystem;
    }

    public void setClassmate_classmatesystem(classmate_ClassmateSystem classmate_classmatesystem) {
        this.classmate_classmatesystem = classmate_classmatesystem;
    }

}