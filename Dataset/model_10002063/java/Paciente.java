





import java.util.List;
import java.util.ArrayList;

public class Paciente  {

    private String rg;
    private String cep;
    private String telefone;
    private String endereco;
    private String nome;
    private int codigo;
    private String cpf;
    private String dataNascimento;



    public Paciente(
        String rg,        String cep,        String telefone,        String endereco,        String nome,        int codigo,        String cpf,        String dataNascimento    ) {
        this.rg = rg;
        this.cep = cep;
        this.telefone = telefone;
        this.endereco = endereco;
        this.nome = nome;
        this.codigo = codigo;
        this.cpf = cpf;
        this.dataNascimento = dataNascimento;
    }


    public String getRg() {
        return rg;
    }

    public void setRg(String rg) {
        this.rg = rg;
    }
    public String getCep() {
        return cep;
    }

    public void setCep(String cep) {
        this.cep = cep;
    }
    public String getTelefone() {
        return telefone;
    }

    public void setTelefone(String telefone) {
        this.telefone = telefone;
    }
    public String getEndereco() {
        return endereco;
    }

    public void setEndereco(String endereco) {
        this.endereco = endereco;
    }
    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }
    public int getCodigo() {
        return codigo;
    }

    public void setCodigo(int codigo) {
        this.codigo = codigo;
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


}