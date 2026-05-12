





import java.util.List;
import java.util.ArrayList;

public class RDBMS_Table  {

    private String name;





    private RDBMS_Scheme rdbms_scheme;




    private RDBMS_PKey rdbms_pkey;




    private RDBMS_Scheme rdbms_scheme;


    public RDBMS_Table(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public RDBMS_Scheme getRdbms_scheme() {
        return rdbms_scheme;
    }

    public void setRdbms_scheme(RDBMS_Scheme rdbms_scheme) {
        this.rdbms_scheme = rdbms_scheme;
    }
    public RDBMS_PKey getRdbms_pkey() {
        return rdbms_pkey;
    }

    public void setRdbms_pkey(RDBMS_PKey rdbms_pkey) {
        this.rdbms_pkey = rdbms_pkey;
    }
    public RDBMS_Scheme getRdbms_scheme() {
        return rdbms_scheme;
    }

    public void setRdbms_scheme(RDBMS_Scheme rdbms_scheme) {
        this.rdbms_scheme = rdbms_scheme;
    }

}