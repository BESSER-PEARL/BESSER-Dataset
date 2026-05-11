





import java.util.List;
import java.util.ArrayList;

public class simpleimperative_VarDecl extends Statement {

    private String name;





    private simpleimperative_Assignation simpleimperative_assignation;


    public simpleimperative_VarDecl(
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

    public simpleimperative_Assignation getSimpleimperative_assignation() {
        return simpleimperative_assignation;
    }

    public void setSimpleimperative_assignation(simpleimperative_Assignation simpleimperative_assignation) {
        this.simpleimperative_assignation = simpleimperative_assignation;
    }

}