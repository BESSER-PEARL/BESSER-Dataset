





import java.util.List;
import java.util.ArrayList;

public class mil_PrintInstruction extends OutputInstruction {

    private String output;



    public mil_PrintInstruction(
        String output    ) {
        super(
        );
        this.output = output;
    }


    public String getOutput() {
        return output;
    }

    public void setOutput(String output) {
        this.output = output;
    }


}