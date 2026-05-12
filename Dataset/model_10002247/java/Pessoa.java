





import java.util.List;
import java.util.ArrayList;

public class Pessoa  {

    private String cpf;
    private String dataInclusao;
    private String sexo;
    private String ultimoAcesso;
    private String dataNascimento;
    private String senha;
    private String email;





    private Endereco endereco;


    public Pessoa(
        String cpf,        String dataInclusao,        String sexo,        String ultimoAcesso,        String dataNascimento,        String senha,        String email    ) {
        this.cpf = cpf;
        this.dataInclusao = dataInclusao;
        this.sexo = sexo;
        this.ultimoAcesso = ultimoAcesso;
        this.dataNascimento = dataNascimento;
        this.senha = senha;
        this.email = email;
    }


    public String getCpf() {
        return cpf;
    }

    public void setCpf(String cpf) {
        this.cpf = cpf;
    }
    public String getDatainclusao() {
        return dataInclusao;
    }

    public void setDatainclusao(String dataInclusao) {
        this.dataInclusao = dataInclusao;
    }
    public String getSexo() {
        return sexo;
    }

    public void setSexo(String sexo) {
        this.sexo = sexo;
    }
    public String getUltimoacesso() {
        return ultimoAcesso;
    }

    public void setUltimoacesso(String ultimoAcesso) {
        this.ultimoAcesso = ultimoAcesso;
    }
    public String getDatanascimento() {
        return dataNascimento;
    }

    public void setDatanascimento(String dataNascimento) {
        this.dataNascimento = dataNascimento;
    }
    public String getSenha() {
        return senha;
    }

    public void setSenha(String senha) {
        this.senha = senha;
    }
    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public Endereco getEndereco() {
        return endereco;
    }

    public void setEndereco(Endereco endereco) {
        this.endereco = endereco;
    }

}