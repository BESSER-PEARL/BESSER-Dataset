





import java.util.List;
import java.util.ArrayList;

public class ConsultaCid  {

    private int ConsultaId;
    private int CidId;





    private Cid cid;




    private List<Consulta> consultas;


    public ConsultaCid(
        int ConsultaId,        int CidId    ) {
        this.ConsultaId = ConsultaId;
        this.CidId = CidId;
        this.consultas = new ArrayList<>();
    }

    public ConsultaCid(
        int ConsultaId,        int CidId        ArrayList<Consulta> consultas    ) {
        this.ConsultaId = ConsultaId;
        this.CidId = CidId;
        this.consultas = consultas;
    }

    public int getConsultaid() {
        return ConsultaId;
    }

    public void setConsultaid(int ConsultaId) {
        this.ConsultaId = ConsultaId;
    }
    public int getCidid() {
        return CidId;
    }

    public void setCidid(int CidId) {
        this.CidId = CidId;
    }

    public Cid getCid() {
        return cid;
    }

    public void setCid(Cid cid) {
        this.cid = cid;
    }
    public List<Consulta> getConsultas() {
        return consultas;
    }

    public void addConsulta(Consulta consulta) {
        this.consultas.add(consulta);
    }

}