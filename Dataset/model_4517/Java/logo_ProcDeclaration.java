





import java.util.List;
import java.util.ArrayList;

public class logo_ProcDeclaration extends Instruction {

    private String name;



    public logo_ProcDeclaration(
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