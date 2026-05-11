





import java.util.List;
import java.util.ArrayList;

public class polybot_modelling_language_Instruction  {

    private String name;
    private String nextInstructionFalse;
    private String nextInstructionTrue;
    private String nextInstruction;





    private polybot_modelling_language_Robot polybot_modelling_language_robot;


    public polybot_modelling_language_Instruction(
        String name,        String nextInstructionFalse,        String nextInstructionTrue,        String nextInstruction    ) {
        this.name = name;
        this.nextInstructionFalse = nextInstructionFalse;
        this.nextInstructionTrue = nextInstructionTrue;
        this.nextInstruction = nextInstruction;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getNextinstructionfalse() {
        return nextInstructionFalse;
    }

    public void setNextinstructionfalse(String nextInstructionFalse) {
        this.nextInstructionFalse = nextInstructionFalse;
    }
    public String getNextinstructiontrue() {
        return nextInstructionTrue;
    }

    public void setNextinstructiontrue(String nextInstructionTrue) {
        this.nextInstructionTrue = nextInstructionTrue;
    }
    public String getNextinstruction() {
        return nextInstruction;
    }

    public void setNextinstruction(String nextInstruction) {
        this.nextInstruction = nextInstruction;
    }

    public polybot_modelling_language_Robot getPolybot_modelling_language_robot() {
        return polybot_modelling_language_robot;
    }

    public void setPolybot_modelling_language_robot(polybot_modelling_language_Robot polybot_modelling_language_robot) {
        this.polybot_modelling_language_robot = polybot_modelling_language_robot;
    }

}