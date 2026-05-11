





import java.util.List;
import java.util.ArrayList;

public class caracteristica_Regra  {

    private String nome;
    private String conteudo;





    private caracteristica_LPS caracteristica_lps;


    public caracteristica_Regra(
        String nome,        String conteudo    ) {
        this.nome = nome;
        this.conteudo = conteudo;
    }


    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }
    public String getConteudo() {
        return conteudo;
    }

    public void setConteudo(String conteudo) {
        this.conteudo = conteudo;
    }

    public caracteristica_LPS getCaracteristica_lps() {
        return caracteristica_lps;
    }

    public void setCaracteristica_lps(caracteristica_LPS caracteristica_lps) {
        this.caracteristica_lps = caracteristica_lps;
    }

}