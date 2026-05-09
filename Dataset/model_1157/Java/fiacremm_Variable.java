





import java.util.List;
import java.util.ArrayList;

public class fiacremm_Variable extends EModelElement {

    private String Name;
    private String initVal;



    public fiacremm_Variable(
        String Name,        String initVal    ) {
        super(
        );
        this.Name = Name;
        this.initVal = initVal;
    }


    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public String getInitval() {
        return initVal;
    }

    public void setInitval(String initVal) {
        this.initVal = initVal;
    }


}