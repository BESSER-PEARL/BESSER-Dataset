





import java.util.List;
import java.util.ArrayList;

public class caracteristica_LPS  {

    private String erro;
    private String nome;
    private String valoresContextuais;



    public caracteristica_LPS(
        String erro,        String nome,        String valoresContextuais    ) {
        this.erro = erro;
        this.nome = nome;
        this.valoresContextuais = valoresContextuais;
    }


    public String getErro() {
        return erro;
    }

    public void setErro(String erro) {
        this.erro = erro;
    }
    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }
    public String getValorescontextuais() {
        return valoresContextuais;
    }

    public void setValorescontextuais(String valoresContextuais) {
        this.valoresContextuais = valoresContextuais;
    }


}