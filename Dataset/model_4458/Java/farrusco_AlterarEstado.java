





import java.util.List;
import java.util.ArrayList;

public class farrusco_AlterarEstado extends Behavior {

    private String Alterar_Decorrer;
    private String Nome;
    private String Alterar_Sucesso;
    private String Alterar_Falha;



    public farrusco_AlterarEstado(
        String Alterar_Decorrer,        String Nome,        String Alterar_Sucesso,        String Alterar_Falha    ) {
        super(
        );
        this.Alterar_Decorrer = Alterar_Decorrer;
        this.Nome = Nome;
        this.Alterar_Sucesso = Alterar_Sucesso;
        this.Alterar_Falha = Alterar_Falha;
    }


    public String getAlterar_decorrer() {
        return Alterar_Decorrer;
    }

    public void setAlterar_decorrer(String Alterar_Decorrer) {
        this.Alterar_Decorrer = Alterar_Decorrer;
    }
    public String getNome() {
        return Nome;
    }

    public void setNome(String Nome) {
        this.Nome = Nome;
    }
    public String getAlterar_sucesso() {
        return Alterar_Sucesso;
    }

    public void setAlterar_sucesso(String Alterar_Sucesso) {
        this.Alterar_Sucesso = Alterar_Sucesso;
    }
    public String getAlterar_falha() {
        return Alterar_Falha;
    }

    public void setAlterar_falha(String Alterar_Falha) {
        this.Alterar_Falha = Alterar_Falha;
    }


}