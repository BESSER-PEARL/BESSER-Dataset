





import java.util.List;
import java.util.ArrayList;

public class Pessanger  {

    private int AadharNo;
    private int Children;



    public Pessanger(
        int AadharNo,        int Children    ) {
        this.AadharNo = AadharNo;
        this.Children = Children;
    }


    public int getAadharno() {
        return AadharNo;
    }

    public void setAadharno(int AadharNo) {
        this.AadharNo = AadharNo;
    }
    public int getChildren() {
        return Children;
    }

    public void setChildren(int Children) {
        this.Children = Children;
    }


}