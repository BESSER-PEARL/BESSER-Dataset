





import java.util.List;
import java.util.ArrayList;

public class rcd_Association  {

    private String lower;
    private String name;
    private String upper;



    public rcd_Association(
        String lower,        String name,        String upper    ) {
        this.lower = lower;
        this.name = name;
        this.upper = upper;
    }


    public String getLower() {
        return lower;
    }

    public void setLower(String lower) {
        this.lower = lower;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getUpper() {
        return upper;
    }

    public void setUpper(String upper) {
        this.upper = upper;
    }


}