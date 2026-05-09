





import java.util.List;
import java.util.ArrayList;

public class appBuilderDSL_InitAction  {






    private appBuilderDSL_Controller appbuilderdsl_controller;




    private List<appBuilderDSL_Instruction> appbuilderdsl_instructions;


    public appBuilderDSL_InitAction(
    ) {
        this.appbuilderdsl_instructions = new ArrayList<>();
    }

    public appBuilderDSL_InitAction(
        ArrayList<appBuilderDSL_Instruction> appbuilderdsl_instructions    ) {
        this.appbuilderdsl_instructions = appbuilderdsl_instructions;
    }


    public appBuilderDSL_Controller getAppbuilderdsl_controller() {
        return appbuilderdsl_controller;
    }

    public void setAppbuilderdsl_controller(appBuilderDSL_Controller appbuilderdsl_controller) {
        this.appbuilderdsl_controller = appbuilderdsl_controller;
    }
    public List<appBuilderDSL_Instruction> getAppbuilderdsl_instructions() {
        return appbuilderdsl_instructions;
    }

    public void addAppbuilderdsl_instruction(Appbuilderdsl_instruction appbuilderdsl_instruction) {
        this.appbuilderdsl_instructions.add(appbuilderdsl_instruction);
    }

}