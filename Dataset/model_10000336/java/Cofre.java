





import java.util.List;
import java.util.ArrayList;

public class Cofre  {

    private float Dinheiro_Armazenado;
    private float Emprestimo_Total;



    public Cofre(
        float Dinheiro_Armazenado,        float Emprestimo_Total    ) {
        this.Dinheiro_Armazenado = Dinheiro_Armazenado;
        this.Emprestimo_Total = Emprestimo_Total;
    }


    public float getDinheiro_armazenado() {
        return Dinheiro_Armazenado;
    }

    public void setDinheiro_armazenado(float Dinheiro_Armazenado) {
        this.Dinheiro_Armazenado = Dinheiro_Armazenado;
    }
    public float getEmprestimo_total() {
        return Emprestimo_Total;
    }

    public void setEmprestimo_total(float Emprestimo_Total) {
        this.Emprestimo_Total = Emprestimo_Total;
    }


}