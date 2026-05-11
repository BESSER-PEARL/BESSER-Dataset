





import java.util.List;
import java.util.ArrayList;

public class caracteristica_LPS  {

    private String nome;
    private String erro;
    private String valoresContextuais;



    public caracteristica_LPS(
        String nome,        String erro,        String valoresContextuais    ) {
        this.nome = nome;
        this.erro = erro;
        this.valoresContextuais = valoresContextuais;
    }


    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }
    public String getErro() {
        return erro;
    }

    public void setErro(String erro) {
        this.erro = erro;
    }
    public String getValorescontextuais() {
        return valoresContextuais;
    }

    public void setValorescontextuais(String valoresContextuais) {
        this.valoresContextuais = valoresContextuais;
    }


}