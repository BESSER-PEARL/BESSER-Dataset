





import java.util.List;
import java.util.ArrayList;

public class Deposito  {

    private String Nome;
    private float Valor;



    public Deposito(
        String Nome,        float Valor    ) {
        this.Nome = Nome;
        this.Valor = Valor;
    }


    public String getNome() {
        return Nome;
    }

    public void setNome(String Nome) {
        this.Nome = Nome;
    }
    public float getValor() {
        return Valor;
    }

    public void setValor(float Valor) {
        this.Valor = Valor;
    }


}