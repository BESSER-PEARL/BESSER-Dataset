





import java.util.List;
import java.util.ArrayList;

public class aadl2_PropertyAssociation extends Element {

    private String append;
    private String constant;



    public aadl2_PropertyAssociation(
        String append,        String constant    ) {
        super(
        );
        this.append = append;
        this.constant = constant;
    }


    public String getAppend() {
        return append;
    }

    public void setAppend(String append) {
        this.append = append;
    }
    public String getConstant() {
        return constant;
    }

    public void setConstant(String constant) {
        this.constant = constant;
    }


}