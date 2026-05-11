





import java.util.List;
import java.util.ArrayList;

public class edu_FunctionDeclaration extends ASTNode {

    private String name;





    private edu_Program edu_program;




    private edu_ReturnValueReference edu_returnvaluereference;




    private edu_Type edu_type;




    private edu_ReturnStatement edu_returnstatement;


    public edu_FunctionDeclaration(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public edu_Program getEdu_program() {
        return edu_program;
    }

    public void setEdu_program(edu_Program edu_program) {
        this.edu_program = edu_program;
    }
    public edu_ReturnValueReference getEdu_returnvaluereference() {
        return edu_returnvaluereference;
    }

    public void setEdu_returnvaluereference(edu_ReturnValueReference edu_returnvaluereference) {
        this.edu_returnvaluereference = edu_returnvaluereference;
    }
    public edu_Type getEdu_type() {
        return edu_type;
    }

    public void setEdu_type(edu_Type edu_type) {
        this.edu_type = edu_type;
    }
    public edu_ReturnStatement getEdu_returnstatement() {
        return edu_returnstatement;
    }

    public void setEdu_returnstatement(edu_ReturnStatement edu_returnstatement) {
        this.edu_returnstatement = edu_returnstatement;
    }

}