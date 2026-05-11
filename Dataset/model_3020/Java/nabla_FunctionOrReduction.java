





import java.util.List;
import java.util.ArrayList;

public class nabla_FunctionOrReduction  {

    private String name;





    private nabla_Instruction nabla_instruction;




    private List<nabla_SimpleVar> nabla_simplevars;




    private List<nabla_Arg> nabla_args;


    public nabla_FunctionOrReduction(
        String name    ) {
        this.name = name;
        this.nabla_simplevars = new ArrayList<>();
        this.nabla_args = new ArrayList<>();
    }

    public nabla_FunctionOrReduction(
        String name        ArrayList<nabla_SimpleVar> nabla_simplevars,        ArrayList<nabla_Arg> nabla_args    ) {
        this.name = name;
        this.nabla_simplevars = nabla_simplevars;
        this.nabla_args = nabla_args;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public nabla_Instruction getNabla_instruction() {
        return nabla_instruction;
    }

    public void setNabla_instruction(nabla_Instruction nabla_instruction) {
        this.nabla_instruction = nabla_instruction;
    }
    public List<nabla_SimpleVar> getNabla_simplevars() {
        return nabla_simplevars;
    }

    public void addNabla_simplevar(Nabla_simplevar nabla_simplevar) {
        this.nabla_simplevars.add(nabla_simplevar);
    }
    public List<nabla_Arg> getNabla_args() {
        return nabla_args;
    }

    public void addNabla_arg(Nabla_arg nabla_arg) {
        this.nabla_args.add(nabla_arg);
    }

}