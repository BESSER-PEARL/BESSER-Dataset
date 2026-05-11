





import java.util.List;
import java.util.ArrayList;

public class klang_VariableDeclaration  {

    private String name;





    private klang_AbstractActor klang_abstractactor;


    public klang_VariableDeclaration(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public klang_AbstractActor getKlang_abstractactor() {
        return klang_abstractactor;
    }

    public void setKlang_abstractactor(klang_AbstractActor klang_abstractactor) {
        this.klang_abstractactor = klang_abstractactor;
    }

}