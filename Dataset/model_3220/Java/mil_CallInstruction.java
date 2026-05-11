





import java.util.List;
import java.util.ArrayList;

public class mil_CallInstruction extends Instruction {






    private mil_LabelInstruction mil_labelinstruction;


    public mil_CallInstruction(
    ) {
        super(
        );
    }



    public mil_LabelInstruction getMil_labelinstruction() {
        return mil_labelinstruction;
    }

    public void setMil_labelinstruction(mil_LabelInstruction mil_labelinstruction) {
        this.mil_labelinstruction = mil_labelinstruction;
    }

}