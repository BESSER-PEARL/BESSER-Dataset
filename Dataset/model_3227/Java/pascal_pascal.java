





import java.util.List;
import java.util.ArrayList;

public class pascal_pascal  {






    private List<pascal_program> pascal_programs;


    public pascal_pascal(
    ) {
        this.pascal_programs = new ArrayList<>();
    }

    public pascal_pascal(
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