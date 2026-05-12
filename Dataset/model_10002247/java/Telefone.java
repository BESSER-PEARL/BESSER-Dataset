





import java.util.List;
import java.util.ArrayList;

public class Telefone  {

    private String numero;
    private int ddd;
    private String tipo;





    private Pessoa pessoa;


    public Telefone(
        String numero,        int ddd,        String tipo    ) {
        this.numero = numero;
        this.ddd = ddd;
        this.tipo = tipo;
    }


    public String getNumero() {
        return numero;
    }

    public void setNumero(String numero) {
        this.numero = numero;
    }
    public int getDdd() {
        return ddd;
    }

    public void setDdd(int ddd) {
        this.ddd = ddd;
    }
    public String getTipo() {
        return tipo;
    }

    public void setTipo(String tipo) {
        this.tipo = tipo;
    }

    public Pessoa getPessoa() {
        return pessoa;
    }

    public void setPessoa(Pessoa pessoa) {
        this.pessoa = pessoa;
    }

}