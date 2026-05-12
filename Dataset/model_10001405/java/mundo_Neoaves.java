





import java.util.List;
import java.util.ArrayList;

public class mundo_Neoaves  {

    private String longitudPatas;
    private String numeroDedosPatas;



    public mundo_Neoaves(
        String longitudPatas,        String numeroDedosPatas    ) {
        this.longitudPatas = longitudPatas;
        this.numeroDedosPatas = numeroDedosPatas;
    }


    public String getLongitudpatas() {
        return longitudPatas;
    }

    public void setLongitudpatas(String longitudPatas) {
        this.longitudPatas = longitudPatas;
    }
    public String getNumerodedospatas() {
        return numeroDedosPatas;
    }

    public void setNumerodedospatas(String numeroDedosPatas) {
        this.numeroDedosPatas = numeroDedosPatas;
    }


}