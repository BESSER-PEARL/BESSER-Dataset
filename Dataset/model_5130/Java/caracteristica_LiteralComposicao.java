





import java.util.List;
import java.util.ArrayList;

public class caracteristica_LiteralComposicao extends Antecedente {

    private String presenca;





    private caracteristica_ElementoCaracteristico caracteristica_elementocaracteristico;


    public caracteristica_LiteralComposicao(
        String presenca    ) {
        super(
        );
        this.presenca = presenca;
    }


    public String getPresenca() {
        return presenca;
    }

    public void setPresenca(String presenca) {
        this.presenca = presenca;
    }

    public caracteristica_ElementoCaracteristico getCaracteristica_elementocaracteristico() {
        return caracteristica_elementocaracteristico;
    }

    public void setCaracteristica_elementocaracteristico(caracteristica_ElementoCaracteristico caracteristica_elementocaracteristico) {
        this.caracteristica_elementocaracteristico = caracteristica_elementocaracteristico;
    }

}