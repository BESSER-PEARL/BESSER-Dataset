





import java.util.List;
import java.util.ArrayList;

public class dml_ID  {

    private String name;





    private dml_S dml_s;




    private dml_F dml_f;


    public dml_ID(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public dml_S getDml_s() {
        return dml_s;
    }

    public void setDml_s(dml_S dml_s) {
        this.dml_s = dml_s;
    }
    public dml_F getDml_f() {
        return dml_f;
    }

    public void setDml_f(dml_F dml_f) {
        this.dml_f = dml_f;
    }

}