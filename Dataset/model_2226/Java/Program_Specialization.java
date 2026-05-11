





import java.util.List;
import java.util.ArrayList;

public class Program_Specialization  {

    private String name;





    private List<Program_Specialization> program_specializations;


    public Program_Specialization(
        String name    ) {
        this.name = name;
        this.program_specializations = new ArrayList<>();
    }

    public Program_Specialization(
        String name        ArrayList<Program_Specialization> program_specializations    ) {
        this.name = name;
        this.program_specializations = program_specializations;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<Program_Specialization> getProgram_specializations() {
        return program_specializations;
    }

    public void addProgram_specialization(Program_specialization program_specialization) {
        this.program_specializations.add(program_specialization);
    }

}