





import java.util.List;
import java.util.ArrayList;

public class iec61131_pous_Program_Declaration extends Library_Element_Declaration {






    private List<Program_Vars> program_varss;


    public iec61131_pous_Program_Declaration(
    ) {
        super(
        );
        this.program_varss = new ArrayList<>();
    }

    public iec61131_pous_Program_Declaration(
        ArrayList<Program_Vars> program_varss    ) {
        this.program_varss = program_varss;
    }


    public List<Program_Vars> getProgram_varss() {
        return program_varss;
    }

    public void addProgram_vars(Program_vars program_vars) {
        this.program_varss.add(program_vars);
    }

}