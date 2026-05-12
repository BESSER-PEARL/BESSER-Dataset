





import java.util.List;
import java.util.ArrayList;

public class Transferencia  {

    private float Valor;
    private String Nome;



    public Transferencia(
        float Valor,        String Nome    ) {
        this.Valor = Valor;
        this.Nome = Nome;
    }


    public float getValor() {
        return Valor;
    }

    public void setValor(float Valor) {
        this.Valor = Valor;
    }
    public String getNome() {
        return Nome;
    }

    public void setNome(String Nome) {
        this.Nome = Nome;
    }


}