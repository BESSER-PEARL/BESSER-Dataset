





import java.util.List;
import java.util.ArrayList;

public class arduino_Bumper_Pressionado extends Condicao {

    private String nome;



    public arduino_Bumper_Pressionado(
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


}