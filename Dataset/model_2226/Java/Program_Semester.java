





import java.util.List;
import java.util.ArrayList;

public class Program_Semester  {

    private String status;
    private String code;
    private String name;





    private Program_Specialization program_specialization;




    private Program_Program program_program;


    public Program_Semester(
        String status,        String code,        String name    ) {
        this.status = status;
        this.code = code;
        this.name = name;
    }


    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }
    public String getCode() {
        return code;
    }

    public void setCode(String code) {
        this.code = code;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public Program_Specialization getProgram_specialization() {
        return program_specialization;
    }

    public void setProgram_specialization(Program_Specialization program_specialization) {
        this.program_specialization = program_specialization;
    }
    public Program_Program getProgram_program() {
        return program_program;
    }

    public void setProgram_program(Program_Program program_program) {
        this.program_program = program_program;
    }

}