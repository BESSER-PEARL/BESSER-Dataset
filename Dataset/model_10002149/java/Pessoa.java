





import java.util.List;
import java.util.ArrayList;

public class Pessoa  {

    private String telefone;
    private String rg;
    private String estadoCivil;
    private String nome;
    private String sexo;
    private String cpf;
    private String endereco;
    private String dataNascimento;



    public Pessoa(
        String telefone,        String rg,        String estadoCivil,        String nome,        String sexo,        String cpf,        String endereco,        String dataNascimento    ) {
        this.telefone = telefone;
        this.rg = rg;
        this.estadoCivil = estadoCivil;
        this.nome = nome;
        this.sexo = sexo;
        this.cpf = cpf;
        this.endereco = endereco;
        this.dataNascimento = dataNascimento;
    }


    public String getTelefone() {
        return telefone;
    }

    public void setTelefone(String telefone) {
        this.telefone = telefone;
    }
    public String getRg() {
        return rg;
    }

    public void setRg(String rg) {
        this.rg = rg;
    }
    public String getEstadocivil() {
        return estadoCivil;
    }

    public void setEstadocivil(String estadoCivil) {
        this.estadoCivil = estadoCivil;
    }
    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }
    public String getSexo() {
        return sexo;
    }

    public void setSexo(String sexo) {
        this.sexo = sexo;
    }
    public String getCpf() {
        return cpf;
    }

    public void setCpf(String cpf) {
        this.cpf = cpf;
    }
    public String getEndereco() {
        return endereco;
    }

    public void setEndereco(String endereco) {
        this.endereco = endereco;
    }
    public String getDatanascimento() {
        return dataNascimento;
    }

    public void setDatanascimento(String dataNascimento) {
        this.dataNascimento = dataNascimento;
    }


}