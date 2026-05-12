





import java.util.List;
import java.util.ArrayList;

public class Cid  {

    private String Codigo;
    private int Id;
    private String Descricao;



    public Cid(
        String Codigo,        int Id,        String Descricao    ) {
        this.Codigo = Codigo;
        this.Id = Id;
        this.Descricao = Descricao;
    }


    public String getCodigo() {
        return Codigo;
    }

    public void setCodigo(String Codigo) {
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


}