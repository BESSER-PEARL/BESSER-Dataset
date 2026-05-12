





import java.util.List;
import java.util.ArrayList;

public class Pessanger  {

    private int Children;
    private int AadharNo;



    public Pessanger(
        int Children,        int AadharNo    ) {
        this.Children = Children;
        this.AadharNo = AadharNo;
    }


    public int getChildren() {
        return Children;
    }

    public void setChildren(int Children) {
        this.Children = Children;
    }
    public int getAadharno() {
        return AadharNo;
    }

    public void setAadharno(int AadharNo) {
        this.AadharNo = AadharNo;
    }


}