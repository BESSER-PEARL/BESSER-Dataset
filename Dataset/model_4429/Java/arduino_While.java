





import java.util.List;
import java.util.ArrayList;

public class arduino_While extends Acoes_Condicionais {

    private String nome;





    private arduino_Acao arduino_acao;


    public arduino_While(
        String nome    ) {
        super(
        );
        this.nome = nome;
    }


    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public arduino_Acao getArduino_acao() {
        return arduino_acao;
    }

    public void setArduino_acao(arduino_Acao arduino_acao) {
        this.arduino_acao = arduino_acao;
    }

}