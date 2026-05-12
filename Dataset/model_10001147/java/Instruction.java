





import java.util.List;
import java.util.ArrayList;

public class Instruction  {






    private List<Program> programs;


    public Instruction(
    ) {
        this.programs = new ArrayList<>();
    }

    public Instruction(
        ArrayList<Program> programs    ) {
        this.programs = programs;
    }


    public List<Program> getPrograms() {
        return programs;
    }

    public void addProgram(Program program) {
        this.programs.add(program);
    }

}