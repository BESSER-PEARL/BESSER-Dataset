





import java.util.List;
import java.util.ArrayList;

public class conta_investimento  {

    private float taxaDeJuros;



    public conta_investimento(
        float taxaDeJuros    ) {
        this.taxaDeJuros = taxaDeJuros;
    }


    public float getTaxadejuros() {
        return taxaDeJuros;
    }

    public void setTaxadejuros(float taxaDeJuros) {
        this.taxaDeJuros = taxaDeJuros;
    }


}