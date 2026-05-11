





import java.util.List;
import java.util.ArrayList;

public class SourceModel_Professor extends Person {






    private SourceModel_Student sourcemodel_student;




    private List<SourceModel_Student> sourcemodel_students;


    public SourceModel_Professor(
    ) {
        super(
        );
        this.sourcemodel_students = new ArrayList<>();
    }

    public SourceModel_Professor(
        ArrayList<SourceModel_Student> sourcemodel_students    ) {
        this.sourcemodel_students = sourcemodel_students;
    }


    public SourceModel_Student getSourcemodel_student() {
        return sourcemodel_student;
    }

    public void setSourcemodel_student(SourceModel_Student sourcemodel_student) {
        this.sourcemodel_student = sourcemodel_student;
    }
    public List<SourceModel_Student> getSourcemodel_students() {
        return sourcemodel_students;
    }

    public void addSourcemodel_student(Sourcemodel_student sourcemodel_student) {
        this.sourcemodel_students.add(sourcemodel_student);
    }

}