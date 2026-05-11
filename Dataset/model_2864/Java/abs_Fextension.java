





import java.util.List;
import java.util.ArrayList;

public class abs_Fextension  {

    private String name;





    private abs_Compilation_Unit abs_compilation_unit;


    public abs_Fextension(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public abs_Compilation_Unit getAbs_compilation_unit() {
        return abs_compilation_unit;
    }

    public void setAbs_compilation_unit(abs_Compilation_Unit abs_compilation_unit) {
        this.abs_compilation_unit = abs_compilation_unit;
    }

}