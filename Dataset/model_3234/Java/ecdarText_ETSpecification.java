





import java.util.List;
import java.util.ArrayList;

public class ecdarText_ETSpecification  {

    private String name;





    private ecdarText_ETFile ecdartext_etfile;


    public ecdarText_ETSpecification(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public ecdarText_ETFile getEcdartext_etfile() {
        return ecdartext_etfile;
    }

    public void setEcdartext_etfile(ecdarText_ETFile ecdartext_etfile) {
        this.ecdartext_etfile = ecdartext_etfile;
    }

}