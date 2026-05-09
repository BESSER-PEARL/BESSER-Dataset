





import java.util.List;
import java.util.ArrayList;

public class dsl_Type extends AbstractFrontElement {

    private String name;





    private dsl_Domain dsl_domain;


    public dsl_Type(
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

    public dsl_Domain getDsl_domain() {
        return dsl_domain;
    }

    public void setDsl_domain(dsl_Domain dsl_domain) {
        this.dsl_domain = dsl_domain;
    }

}