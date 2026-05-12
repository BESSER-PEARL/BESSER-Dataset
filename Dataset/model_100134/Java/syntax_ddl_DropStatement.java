





import java.util.List;
import java.util.ArrayList;

public class syntax_ddl_DropStatement extends DefinitionStatement {

    private String range;
    private String target;



    public syntax_ddl_DropStatement(
        String range,        String target    ) {
        super(
        );
        this.range = range;
        this.target = target;
    }


    public String getRange() {
        return range;
    }

    public void setRange(String range) {
        this.range = range;
    }
    public String getTarget() {
        return target;
    }

    public void setTarget(String target) {
        this.target = target;
    }


}