





import java.util.List;
import java.util.ArrayList;

public class architecture_Variable  {

    private String name;





    private architecture_Operation architecture_operation;




    private architecture_Architecture architecture_architecture;


    public architecture_Variable(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public architecture_Operation getArchitecture_operation() {
        return architecture_operation;
    }

    public void setArchitecture_operation(architecture_Operation architecture_operation) {
        this.architecture_operation = architecture_operation;
    }
    public architecture_Architecture getArchitecture_architecture() {
        return architecture_architecture;
    }

    public void setArchitecture_architecture(architecture_Architecture architecture_architecture) {
        this.architecture_architecture = architecture_architecture;
    }

}