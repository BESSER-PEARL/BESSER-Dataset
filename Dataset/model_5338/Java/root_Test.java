





import java.util.List;
import java.util.ArrayList;

public class root_Test  {

    private String name;
    private int att1;
    private int att2;



    public root_Test(
        String name,        int att1,        int att2    ) {
        this.name = name;
        this.att1 = att1;
        this.att2 = att2;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getAtt1() {
        return att1;
    }

    public void setAtt1(int att1) {
        this.att1 = att1;
    }
    public int getAtt2() {
        return att2;
    }

    public void setAtt2(int att2) {
        this.att2 = att2;
    }


}