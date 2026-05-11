





import java.util.List;
import java.util.ArrayList;

public class kmLogo_ProcDeclaration extends Instruction {

    private String name;



    public kmLogo_ProcDeclaration(
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