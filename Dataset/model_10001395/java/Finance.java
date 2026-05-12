





import java.util.List;
import java.util.ArrayList;

public class Finance  {

    private String coast;
    private String Cname;



    public Finance(
        String coast,        String Cname    ) {
        this.coast = coast;
        this.Cname = Cname;
    }


    public String getCoast() {
        return coast;
    }

    public void setCoast(String coast) {
        this.coast = coast;
    }
    public String getCname() {
        return Cname;
    }

    public void setCname(String Cname) {
        this.Cname = Cname;
    }


}