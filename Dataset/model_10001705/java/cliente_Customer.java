




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class cliente_Customer  {

    private String nome;
    private String email;
    private LocalDate dataNascimento;
    private String numeroTel;
    private String endere_o;





    private Login login;


    public cliente_Customer(
        String nome,        String email,        LocalDate dataNascimento,        String numeroTel,        String endere_o    ) {
        this.nome = nome;
        this.email = email;
        this.dataNascimento = dataNascimento;
        this.numeroTel = numeroTel;
        this.endere_o = endere_o;
    }


    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }
    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }
    public LocalDate getDatanascimento() {
        return dataNascimento;
    }

    public void setDatanascimento(LocalDate dataNascimento) {
        this.dataNascimento = dataNascimento;
    }
    public String getNumerotel() {
        return numeroTel;
    }

    public void setNumerotel(String numeroTel) {
        this.numeroTel = numeroTel;
    }
    public String getEndere_o() {
        return endere_o;
    }

    public void setEndere_o(String endere_o) {
        this.endere_o = endere_o;
    }

    public Login getLogin() {
        return login;
    }

    public void setLogin(Login login) {
        this.login = login;
    }

}