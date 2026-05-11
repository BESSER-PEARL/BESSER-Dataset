





import java.util.List;
import java.util.ArrayList;

public class sql_JRParameter extends Prms {

    private String jrprm;





    private sql_Prms sql_prms;


    public sql_JRParameter(
        String jrprm    ) {
        super(
        );
        this.jrprm = jrprm;
    }


    public String getJrprm() {
        return jrprm;
    }

    public void setJrprm(String jrprm) {
        this.jrprm = jrprm;
    }

    public sql_Prms getSql_prms() {
        return sql_prms;
    }

    public void setSql_prms(sql_Prms sql_prms) {
        this.sql_prms = sql_prms;
    }

}