





import java.util.List;
import java.util.ArrayList;

public class Especialidade  {

    private String Descricao;
    private int Id;





    private List<Agenda> agendas;


    public Especialidade(
        String Descricao,        int Id    ) {
        this.Descricao = Descricao;
        this.Id = Id;
        this.agendas = new ArrayList<>();
    }

    public Especialidade(
        String Descricao,        int Id        ArrayList<Agenda> agendas    ) {
        this.Descricao = Descricao;
        this.Id = Id;
        this.agendas = agendas;
    }

    public String getDescricao() {
        return Descricao;
    }

    public void setDescricao(String Descricao) {
        this.Descricao = Descricao;
    }
    public int getId() {
        return Id;
    }

    public void setId(int Id) {
        this.Id = Id;
    }

    public List<Agenda> getAgendas() {
        return agendas;
    }

    public void addAgenda(Agenda agenda) {
        this.agendas.add(agenda);
    }

}