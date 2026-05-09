





import java.util.List;
import java.util.ArrayList;

public class vhdl_ComponentInstantiationStatement extends ArchitectureStatement {

    private String name;



    public vhdl_ComponentInstantiationStatement(
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