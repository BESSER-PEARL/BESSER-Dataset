





import java.util.List;
import java.util.ArrayList;

public class Paciente  {






    private TipoSanguineo tiposanguineo;




    private List<Interacao> interacaos;


    public Paciente(
    ) {
        this.interacaos = new ArrayList<>();
    }

    public Paciente(
        ArrayList<Interacao> interacaos    ) {
        this.interacaos = interacaos;
    }


    public TipoSanguineo getTiposanguineo() {
        return tiposanguineo;
    }

    public void setTiposanguineo(TipoSanguineo tiposanguineo) {
        this.tiposanguineo = tiposanguineo;
    }
    public List<Interacao> getInteracaos() {
        return interacaos;
    }

    public void addInteracao(Interacao interacao) {
        this.interacaos.add(interacao);
    }

}