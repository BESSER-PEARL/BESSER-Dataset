





import java.util.List;
import java.util.ArrayList;

public class debugSeq_VariableDeclaration extends Statement {

    private String name;



    public debugSeq_VariableDeclaration(
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