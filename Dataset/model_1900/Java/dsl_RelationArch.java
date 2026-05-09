





import java.util.List;
import java.util.ArrayList;

public class dsl_RelationArch  {

    private String name;
    private String source;





    private dsl_Architecture dsl_architecture;


    public dsl_RelationArch(
        String name,        String source    ) {
        this.name = name;
        this.source = source;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getSource() {
        return source;
    }

    public void setSource(String source) {
        this.source = source;
    }

    public dsl_Architecture getDsl_architecture() {
        return dsl_architecture;
    }

    public void setDsl_architecture(dsl_Architecture dsl_architecture) {
        this.dsl_architecture = dsl_architecture;
    }

}