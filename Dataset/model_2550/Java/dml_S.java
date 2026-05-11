





import java.util.List;
import java.util.ArrayList;

public class dml_S  {

    private String src;
    private String cwd;





    private dml_D dml_d;




    private dml_F dml_f;


    public dml_S(
        String src,        String cwd    ) {
        this.src = src;
        this.cwd = cwd;
    }


    public String getSrc() {
        return src;
    }

    public void setSrc(String src) {
        this.src = src;
    }
    public String getCwd() {
        return cwd;
    }

    public void setCwd(String cwd) {
        this.cwd = cwd;
    }

    public dml_D getDml_d() {
        return dml_d;
    }

    public void setDml_d(dml_D dml_d) {
        this.dml_d = dml_d;
    }
    public dml_F getDml_f() {
        return dml_f;
    }

    public void setDml_f(dml_F dml_f) {
        this.dml_f = dml_f;
    }

}