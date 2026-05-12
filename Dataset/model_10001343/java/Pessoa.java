





import java.util.List;
import java.util.ArrayList;

public class Pessoa  {

    private String Nome;
    private int id;
    private int idade;



    public Pessoa(
        String Nome,        int id,        int idade    ) {
        this.Nome = Nome;
        this.id = id;
        this.idade = idade;
    }


    public String getNome() {
        return Nome;
    }

    public void setNome(String Nome) {
        this.Nome = Nome;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public int getIdade() {
        return idade;
    }

    public void setIdade(int idade) {
        this.idade = idade;
    }


}