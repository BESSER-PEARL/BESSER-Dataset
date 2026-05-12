





import java.util.List;
import java.util.ArrayList;

public class syntax_ddl_DisconnectStatement extends DefinitionStatement {

    private String target;



    public syntax_ddl_DisconnectStatement(
        String target    ) {
        super(
        );
        this.target = target;
    }


    public String getTarget() {
        return target;
    }

    public void setTarget(String target) {
        this.target = target;
    }


}