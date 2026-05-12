





import java.util.List;
import java.util.ArrayList;

public class Consulta  {

    private String Observacoes;
    private None Cirurgiao;
    private String DataHora;
    private int ConsultaId;
    private String Situacao;
    private None Cliente;





    private Cliente cliente;




    private Cirurgiao cirurgiao;


    public Consulta(
        String Observacoes,        None Cirurgiao,        String DataHora,        int ConsultaId,        String Situacao,        None Cliente    ) {
        this.Observacoes = Observacoes;
        this.Cirurgiao = Cirurgiao;
        this.DataHora = DataHora;
        this.ConsultaId = ConsultaId;
        this.Situacao = Situacao;
        this.Cliente = Cliente;
    }


    public String getObservacoes() {
        return Observacoes;
    }

    public void setObservacoes(String Observacoes) {
        this.Observacoes = Observacoes;
    }
    public None getCirurgiao() {
        return Cirurgiao;
    }

    public void setCirurgiao(None Cirurgiao) {
        this.Cirurgiao = Cirurgiao;
    }
    public String getDatahora() {
        return DataHora;
    }

    public void setDatahora(String DataHora) {
        this.DataHora = DataHora;
    }
    public int getConsultaid() {
        return ConsultaId;
    }

    public void setConsultaid(int ConsultaId) {
        this.ConsultaId = ConsultaId;
    }
    public String getSituacao() {
        return Situacao;
    }

    public void setSituacao(String Situacao) {
        this.Situacao = Situacao;
    }
    public None getCliente() {
        return Cliente;
    }

    public void setCliente(None Cliente) {
        this.Cliente = Cliente;
    }

    public Cliente getCliente() {
        return cliente;
    }

    public void setCliente(Cliente cliente) {
        this.cliente = cliente;
    }
    public Cirurgiao getCirurgiao() {
        return cirurgiao;
    }

    public void setCirurgiao(Cirurgiao cirurgiao) {
        this.cirurgiao = cirurgiao;
    }

}