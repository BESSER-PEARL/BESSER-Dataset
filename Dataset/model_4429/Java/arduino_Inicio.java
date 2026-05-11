





import java.util.List;
import java.util.ArrayList;

public class arduino_Inicio extends Acao {

    private boolean evitarObstaculo;
    private String nome;



    public arduino_Inicio(
        boolean evitarObstaculo,        String nome    ) {
        super(
        );
        this.evitarObstaculo = evitarObstaculo;
        this.nome = nome;
    }


    public boolean getEvitarobstaculo() {
        return evitarObstaculo;
    }

    public void setEvitarobstaculo(boolean evitarObstaculo) {
        this.evitarObstaculo = evitarObstaculo;
    }
    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }


}