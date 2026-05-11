





import java.util.List;
import java.util.ArrayList;

public class aadl2_PropertyAssociation extends Element {

    private String constant;
    private String append;



    public aadl2_PropertyAssociation(
        String constant,        String append    ) {
        super(
        );
        this.constant = constant;
        this.append = append;
    }


    public String getConstant() {
        return constant;
    }

    public void setConstant(String constant) {
        this.constant = constant;
    }
    public String getAppend() {
        return append;
    }

    public void setAppend(String append) {
        this.append = append;
    }


}