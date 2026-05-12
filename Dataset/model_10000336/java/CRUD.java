





import java.util.List;
import java.util.ArrayList;

public class CRUD  {

    private String Adicionar_Conta;
    private String Remover_Conta;



    public CRUD(
        String Adicionar_Conta,        String Remover_Conta    ) {
        this.Adicionar_Conta = Adicionar_Conta;
        this.Remover_Conta = Remover_Conta;
    }


    public String getAdicionar_conta() {
        return Adicionar_Conta;
    }

    public void setAdicionar_conta(String Adicionar_Conta) {
        this.Adicionar_Conta = Adicionar_Conta;
    }
    public String getRemover_conta() {
        return Remover_Conta;
    }

    public void setRemover_conta(String Remover_Conta) {
        this.Remover_Conta = Remover_Conta;
    }


}