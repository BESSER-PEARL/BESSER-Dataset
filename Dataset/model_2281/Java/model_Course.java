





import java.util.List;
import java.util.ArrayList;

public class model_Course  {

    private String name;
    private int ID;





    private model_Student model_student;


    public model_Course(
        String name,        int ID    ) {
        this.name = name;
        this.ID = ID;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getId() {
        return ID;
    }

    public void setId(int ID) {
        this.ID = ID;
    }

    public model_Student getModel_student() {
        return model_student;
    }

    public void setModel_student(model_Student model_student) {
        this.model_student = model_student;
    }

}