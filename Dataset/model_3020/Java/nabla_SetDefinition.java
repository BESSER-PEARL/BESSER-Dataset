





import java.util.List;
import java.util.ArrayList;

public class nabla_SetDefinition extends Instruction {

    private String name;



    public nabla_SetDefinition(
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