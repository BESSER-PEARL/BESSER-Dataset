





import java.util.List;
import java.util.ArrayList;

public class myDsl_Type extends AbstractFrontElement {

    private String name;





    private myDsl_Domain mydsl_domain;


    public myDsl_Type(
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

    public myDsl_Domain getMydsl_domain() {
        return mydsl_domain;
    }

    public void setMydsl_domain(myDsl_Domain mydsl_domain) {
        this.mydsl_domain = mydsl_domain;
    }

}