





import java.util.List;
import java.util.ArrayList;

public class PyDslRep_MoveCollection extends Entity {

    private String name;
    private boolean concurrent;





    private PyDslRep_Environment pydslrep_environment;


    public PyDslRep_MoveCollection(
        String name,        boolean concurrent    ) {
        super(
        );
        this.name = name;
        this.concurrent = concurrent;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getConcurrent() {
        return concurrent;
    }

    public void setConcurrent(boolean concurrent) {
        this.concurrent = concurrent;
    }

    public PyDslRep_Environment getPydslrep_environment() {
        return pydslrep_environment;
    }

    public void setPydslrep_environment(PyDslRep_Environment pydslrep_environment) {
        this.pydslrep_environment = pydslrep_environment;
    }

}