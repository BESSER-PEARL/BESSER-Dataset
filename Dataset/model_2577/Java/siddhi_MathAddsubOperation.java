





import java.util.List;
import java.util.ArrayList;

public class siddhi_MathAddsubOperation extends MathOperation {

    private String add;
    private String substract;



    public siddhi_MathAddsubOperation(
        String add,        String substract    ) {
        super(
        );
        this.add = add;
        this.substract = substract;
    }


    public String getAdd() {
        return add;
    }

    public void setAdd(String add) {
        this.add = add;
    }
    public String getSubstract() {
        return substract;
    }

    public void setSubstract(String substract) {
        this.substract = substract;
    }


}