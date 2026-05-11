





import java.util.List;
import java.util.ArrayList;

public class caracteristica_ElementoDeProduto  {

    private String nome;





    private caracteristica_Elemento caracteristica_elemento;




    private caracteristica_LPS caracteristica_lps;


    public caracteristica_ElementoDeProduto(
        String nome    ) {
        this.nome = nome;
    }


    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public caracteristica_Elemento getCaracteristica_elemento() {
        return caracteristica_elemento;
    }

    public void setCaracteristica_elemento(caracteristica_Elemento caracteristica_elemento) {
        this.caracteristica_elemento = caracteristica_elemento;
    }
    public caracteristica_LPS getCaracteristica_lps() {
        return caracteristica_lps;
    }

    public void setCaracteristica_lps(caracteristica_LPS caracteristica_lps) {
        this.caracteristica_lps = caracteristica_lps;
    }

}