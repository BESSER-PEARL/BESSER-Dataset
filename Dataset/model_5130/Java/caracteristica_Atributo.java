





import java.util.List;
import java.util.ArrayList;

public class caracteristica_Atributo extends Elemento {

    private String tipoValor;





    private caracteristica_LPS caracteristica_lps;




    private caracteristica_Caracteristica caracteristica_caracteristica;




    private caracteristica_Caracteristica caracteristica_caracteristica;


    public caracteristica_Atributo(
        String tipoValor    ) {
        super(
        );
        this.tipoValor = tipoValor;
    }


    public String getTipovalor() {
        return tipoValor;
    }

    public void setTipovalor(String tipoValor) {
        this.tipoValor = tipoValor;
    }

    public caracteristica_LPS getCaracteristica_lps() {
        return caracteristica_lps;
    }

    public void setCaracteristica_lps(caracteristica_LPS caracteristica_lps) {
        this.caracteristica_lps = caracteristica_lps;
    }
    public caracteristica_Caracteristica getCaracteristica_caracteristica() {
        return caracteristica_caracteristica;
    }

    public void setCaracteristica_caracteristica(caracteristica_Caracteristica caracteristica_caracteristica) {
        this.caracteristica_caracteristica = caracteristica_caracteristica;
    }
    public caracteristica_Caracteristica getCaracteristica_caracteristica() {
        return caracteristica_caracteristica;
    }

    public void setCaracteristica_caracteristica(caracteristica_Caracteristica caracteristica_caracteristica) {
        this.caracteristica_caracteristica = caracteristica_caracteristica;
    }

}