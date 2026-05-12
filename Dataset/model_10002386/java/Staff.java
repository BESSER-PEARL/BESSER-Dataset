





import java.util.List;
import java.util.ArrayList;

public class Staff  {

    private String contato;
    private int TrabalhoTipo;
    private String nome;
    private String staff_Id;



    public Staff(
        String contato,        int TrabalhoTipo,        String nome,        String staff_Id    ) {
        this.contato = contato;
        this.TrabalhoTipo = TrabalhoTipo;
        this.nome = nome;
        this.staff_Id = staff_Id;
    }


    public String getContato() {
        return contato;
    }

    public void setContato(String contato) {
        this.contato = contato;
    }
    public int getTrabalhotipo() {
        return TrabalhoTipo;
    }

    public void setTrabalhotipo(int TrabalhoTipo) {
        this.TrabalhoTipo = TrabalhoTipo;
    }
    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }
    public String getStaff_id() {
        return staff_Id;
    }

    public void setStaff_id(String staff_Id) {
        this.staff_Id = staff_Id;
    }


}