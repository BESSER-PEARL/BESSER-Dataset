





import java.util.List;
import java.util.ArrayList;

public class farrusco_Servo extends Actuate {

    private int Posicao_Minima;
    private String Nome;
    private int Passo_a_Passo;
    private int Posicao_Maxima;



    public farrusco_Servo(
        int Posicao_Minima,        String Nome,        int Passo_a_Passo,        int Posicao_Maxima    ) {
        super(
        );
        this.Posicao_Minima = Posicao_Minima;
        this.Nome = Nome;
        this.Passo_a_Passo = Passo_a_Passo;
        this.Posicao_Maxima = Posicao_Maxima;
    }


    public int getPosicao_minima() {
        return Posicao_Minima;
    }

    public void setPosicao_minima(int Posicao_Minima) {
        this.Posicao_Minima = Posicao_Minima;
    }
    public String getNome() {
        return Nome;
    }

    public void setNome(String Nome) {
        this.Nome = Nome;
    }
    public int getPasso_a_passo() {
        return Passo_a_Passo;
    }

    public void setPasso_a_passo(int Passo_a_Passo) {
        this.Passo_a_Passo = Passo_a_Passo;
    }
    public int getPosicao_maxima() {
        return Posicao_Maxima;
    }

    public void setPosicao_maxima(int Posicao_Maxima) {
        this.Posicao_Maxima = Posicao_Maxima;
    }


}