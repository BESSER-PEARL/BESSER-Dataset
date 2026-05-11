





import java.util.List;
import java.util.ArrayList;

public class caracteristica_Elemento  {

    private String nome;





    private caracteristica_LPS caracteristica_lps;


    public caracteristica_Elemento(
        String nome    ) {
        this.nome = nome;
    }


    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public caracteristica_LPS getCaracteristica_lps() {
        return caracteristica_lps;
    }

    public void setCaracteristica_lps(caracteristica_LPS caracteristica_lps) {
        this.caracteristica_lps = caracteristica_lps;
    }

}