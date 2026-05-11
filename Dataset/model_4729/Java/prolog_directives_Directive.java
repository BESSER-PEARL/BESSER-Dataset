





import java.util.List;
import java.util.ArrayList;

public class prolog_directives_Directive extends Clause {

    private String name;



    public prolog_directives_Directive(
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