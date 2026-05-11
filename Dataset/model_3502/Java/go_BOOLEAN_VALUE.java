





import java.util.List;
import java.util.ArrayList;

public class go_BOOLEAN_VALUE  {

    private String verdadeiro;
    private String falso;





    private go_LITERAIS_BASICOS go_literais_basicos;


    public go_BOOLEAN_VALUE(
        String verdadeiro,        String falso    ) {
        this.verdadeiro = verdadeiro;
        this.falso = falso;
    }


    public String getVerdadeiro() {
        return verdadeiro;
    }

    public void setVerdadeiro(String verdadeiro) {
        this.verdadeiro = verdadeiro;
    }
    public String getFalso() {
        return falso;
    }

    public void setFalso(String falso) {
        this.falso = falso;
    }

    public go_LITERAIS_BASICOS getGo_literais_basicos() {
        return go_literais_basicos;
    }

    public void setGo_literais_basicos(go_LITERAIS_BASICOS go_literais_basicos) {
        this.go_literais_basicos = go_literais_basicos;
    }

}