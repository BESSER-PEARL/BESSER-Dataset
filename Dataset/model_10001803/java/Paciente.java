





import java.util.List;
import java.util.ArrayList;

public class Paciente  {

    private String Endereco;
    private String Sexo;
    private String Nacionalidade;
    private None CPF;
    private String Email;
    private int CPF1;
    private int Telefone;
    private int Celular;
    private int RG;
    private String Sobrenome;
    private int CEP;
    private String Cidade;
    private String EstadoCivil;
    private String Estado;
    private String DataNascimento;
    private String ConvenioMedico;
    private String Nome;



    public Paciente(
        String Endereco,        String Sexo,        String Nacionalidade,        None CPF,        String Email,        int CPF1,        int Telefone,        int Celular,        int RG,        String Sobrenome,        int CEP,        String Cidade,        String EstadoCivil,        String Estado,        String DataNascimento,        String ConvenioMedico,        String Nome    ) {
        this.Endereco = Endereco;
        this.Sexo = Sexo;
        this.Nacionalidade = Nacionalidade;
        this.CPF = CPF;
        this.Email = Email;
        this.CPF1 = CPF1;
        this.Telefone = Telefone;
        this.Celular = Celular;
        this.RG = RG;
        this.Sobrenome = Sobrenome;
        this.CEP = CEP;
        this.Cidade = Cidade;
        this.EstadoCivil = EstadoCivil;
        this.Estado = Estado;
        this.DataNascimento = DataNascimento;
        this.ConvenioMedico = ConvenioMedico;
        this.Nome = Nome;
    }


    public String getEndereco() {
        return Endereco;
    }

    public void setEndereco(String Endereco) {
        this.Endereco = Endereco;
    }
    public String getSexo() {
        return Sexo;
    }

    public void setSexo(String Sexo) {
        this.Sexo = Sexo;
    }
    public String getNacionalidade() {
        return Nacionalidade;
    }

    public void setNacionalidade(String Nacionalidade) {
        this.Nacionalidade = Nacionalidade;
    }
    public None getCpf() {
        return CPF;
    }

    public void setCpf(None CPF) {
        this.CPF = CPF;
    }
    public String getEmail() {
        return Email;
    }

    public void setEmail(String Email) {
        this.Email = Email;
    }
    public int getCpf1() {
        return CPF1;
    }

    public void setCpf1(int CPF1) {
        this.CPF1 = CPF1;
    }
    public int getTelefone() {
        return Telefone;
    }

    public void setTelefone(int Telefone) {
        this.Telefone = Telefone;
    }
    public int getCelular() {
        return Celular;
    }

    public void setCelular(int Celular) {
        this.Celular = Celular;
    }
    public int getRg() {
        return RG;
    }

    public void setRg(int RG) {
        this.RG = RG;
    }
    public String getSobrenome() {
        return Sobrenome;
    }

    public void setSobrenome(String Sobrenome) {
        this.Sobrenome = Sobrenome;
    }
    public int getCep() {
        return CEP;
    }

    public void setCep(int CEP) {
        this.CEP = CEP;
    }
    public String getCidade() {
        return Cidade;
    }

    public void setCidade(String Cidade) {
        this.Cidade = Cidade;
    }
    public String getEstadocivil() {
        return EstadoCivil;
    }

    public void setEstadocivil(String EstadoCivil) {
        this.EstadoCivil = EstadoCivil;
    }
    public String getEstado() {
        return Estado;
    }

    public void setEstado(String Estado) {
        this.Estado = Estado;
    }
    public String getDatanascimento() {
        return DataNascimento;
    }

    public void setDatanascimento(String DataNascimento) {
        this.DataNascimento = DataNascimento;
    }
    public String getConveniomedico() {
        return ConvenioMedico;
    }

    public void setConveniomedico(String ConvenioMedico) {
        this.ConvenioMedico = ConvenioMedico;
    }
    public String getNome() {
        return Nome;
    }

    public void setNome(String Nome) {
        this.Nome = Nome;
    }


}