





import java.util.List;
import java.util.ArrayList;

public class Usuario  {

    private String nome;
    private String senha;
    private String cpf;
    private String dataNascimento;
    private String peso;



    public Usuario(
        String nome,        String senha,        String cpf,        String dataNascimento,        String peso    ) {
        this.nome = nome;
        this.senha = senha;
        this.cpf = cpf;
        this.dataNascimento = dataNascimento;
        this.peso = peso;
    }


    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }
    public String getSenha() {
        return senha;
    }

    public void setSenha(String senha) {
        this.senha = senha;
    }
    public String getCpf() {
        return cpf;
    }

    public void setCpf(String cpf) {
        this.cpf = cpf;
    }
    public String getDatanascimento() {
        return dataNascimento;
    }

    public void setDatanascimento(String dataNascimento) {
        this.dataNascimento = dataNascimento;
    }
    public String getPeso() {
        return peso;
    }

    public void setPeso(String peso) {
        this.peso = peso;
    }


}