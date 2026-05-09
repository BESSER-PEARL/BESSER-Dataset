





import java.util.List;
import java.util.ArrayList;

public class yyk_Output  {

    private String id;





    private yyk_Base yyk_base;




    private yyk_Bar yyk_bar;


    public yyk_Output(
        String id    ) {
        this.id = id;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public yyk_Base getYyk_base() {
        return yyk_base;
    }

    public void setYyk_base(yyk_Base yyk_base) {
        this.yyk_base = yyk_base;
    }
    public yyk_Bar getYyk_bar() {
        return yyk_bar;
    }

    public void setYyk_bar(yyk_Bar yyk_bar) {
        this.yyk_bar = yyk_bar;
    }

}