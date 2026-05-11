





import java.util.List;
import java.util.ArrayList;

public class leek_FunctionDeclaration extends Expression, Statement {

    private String name;



    public leek_FunctionDeclaration(
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