





import java.util.List;
import java.util.ArrayList;

public class caracteristica_ExpressaoRelacional extends Antecedente {

    private String operadorRelacional;
    private String valor;





    private caracteristica_Atributo caracteristica_atributo;


    public caracteristica_ExpressaoRelacional(
        String operadorRelacional,        String valor    ) {
        super(
        );
        this.operadorRelacional = operadorRelacional;
        this.valor = valor;
    }


    public String getOperadorrelacional() {
        return operadorRelacional;
    }

    public void setOperadorrelacional(String operadorRelacional) {
        this.operadorRelacional = operadorRelacional;
    }
    public String getValor() {
        return valor;
    }

    public void setValor(String valor) {
        this.valor = valor;
    }

    public caracteristica_Atributo getCaracteristica_atributo() {
        return caracteristica_atributo;
    }

    public void setCaracteristica_atributo(caracteristica_Atributo caracteristica_atributo) {
        this.caracteristica_atributo = caracteristica_atributo;
    }

}