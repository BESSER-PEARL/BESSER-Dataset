





import java.util.List;
import java.util.ArrayList;

public class Paciente  {

    private int Id;
    private String Nome;
    private String NomeMae;
    private String CPF;
    private String DataNascimento;



    public Paciente(
        int Id,        String Nome,        String NomeMae,        String CPF,        String DataNascimento    ) {
        this.Id = Id;
        this.Nome = Nome;
        this.NomeMae = NomeMae;
        this.CPF = CPF;
        this.DataNascimento = DataNascimento;
    }


    public int getId() {
        return Id;
    }

    public void setId(int Id) {
        this.Id = Id;
    }
    public String getNome() {
        return Nome;
    }

    public void setNome(String Nome) {
        this.Nome = Nome;
    }
    public String getNomemae() {
        return NomeMae;
    }

    public void setNomemae(String NomeMae) {
        this.NomeMae = NomeMae;
    }
    public String getCpf() {
        return CPF;
    }

    public void setCpf(String CPF) {
        this.CPF = CPF;
    }
    public String getDatanascimento() {
        return DataNascimento;
    }

    public void setDatanascimento(String DataNascimento) {
        this.DataNascimento = DataNascimento;
    }


}