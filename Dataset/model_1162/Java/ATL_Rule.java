





import java.util.List;
import java.util.ArrayList;

public class ATL_Rule extends ModuleElement {

    private String name;





    private OutPattern outpattern;


    public ATL_Rule(
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

    public OutPattern getOutpattern() {
        return outpattern;
    }

    public void setOutpattern(OutPattern outpattern) {
        this.outpattern = outpattern;
    }

}