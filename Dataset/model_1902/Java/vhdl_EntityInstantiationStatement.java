





import java.util.List;
import java.util.ArrayList;

public class vhdl_EntityInstantiationStatement extends ArchitectureStatement {

    private String name;



    public vhdl_EntityInstantiationStatement(
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