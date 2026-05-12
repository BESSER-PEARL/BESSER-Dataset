





import java.util.List;
import java.util.ArrayList;

public class Exame  {

    private int Id;
    private String Descricao;
    private String Codigo;



    public Exame(
        int Id,        String Descricao,        String Codigo    ) {
        this.Id = Id;
        this.Descricao = Descricao;
        this.Codigo = Codigo;
    }


    public int getId() {
        return Id;
    }

    public void setId(int Id) {
        this.Id = Id;
    }
    public String getDescricao() {
        return Descricao;
    }

    public void setDescricao(String Descricao) {
        this.Descricao = Descricao;
    }
    public String getCodigo() {
        return Codigo;
    }

    public void setCodigo(String Codigo) {
        this.Codigo = Codigo;
    }


}