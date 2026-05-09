





import java.util.List;
import java.util.ArrayList;

public class appBuilderDSL_UiAction extends Action {

    private String name;





    private List<appBuilderDSL_Instruction> appbuilderdsl_instructions;


    public appBuilderDSL_UiAction(
        String name    ) {
        super(
        );
        this.name = name;
        this.appbuilderdsl_instructions = new ArrayList<>();
    }

    public appBuilderDSL_UiAction(
        String name        ArrayList<appBuilderDSL_Instruction> appbuilderdsl_instructions    ) {
        this.name = name;
        this.appbuilderdsl_instructions = appbuilderdsl_instructions;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<appBuilderDSL_Instruction> getAppbuilderdsl_instructions() {
        return appbuilderdsl_instructions;
    }

    public void addAppbuilderdsl_instruction(Appbuilderdsl_instruction appbuilderdsl_instruction) {
        this.appbuilderdsl_instructions.add(appbuilderdsl_instruction);
    }

}