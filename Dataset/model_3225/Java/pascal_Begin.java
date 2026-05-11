





import java.util.List;
import java.util.ArrayList;

public class pascal_Begin  {






    private List<pascal_program> pascal_programs;


    public pascal_Begin(
    ) {
        this.pascal_programs = new ArrayList<>();
    }

    public pascal_Begin(
        ArrayList<pascal_program> pascal_programs    ) {
        this.pascal_programs = pascal_programs;
    }


    public List<pascal_program> getPascal_programs() {
        return pascal_programs;
    }

    public void addPascal_program(Pascal_program pascal_program) {
        this.pascal_programs.add(pascal_program);
    }

}