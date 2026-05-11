





import java.util.List;
import java.util.ArrayList;

public class mil_LabelInstruction extends Instruction {

    private String name;



    public mil_LabelInstruction(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}