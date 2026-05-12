





import java.util.List;
import java.util.ArrayList;

public class ConsultaMedicamento  {

    private String Posologia;
    private None MedicamentoId;





    private Medicamento medicamento;




    private Consulta consulta;


    public ConsultaMedicamento(
        String Posologia,        None MedicamentoId    ) {
        this.Posologia = Posologia;
        this.MedicamentoId = MedicamentoId;
    }


    public String getPosologia() {
        return Posologia;
    }

    public void setPosologia(String Posologia) {
        this.Posologia = Posologia;
    }
    public None getMedicamentoid() {
        return MedicamentoId;
    }

    public void setMedicamentoid(None MedicamentoId) {
        this.MedicamentoId = MedicamentoId;
    }

    public Medicamento getMedicamento() {
        return medicamento;
    }

    public void setMedicamento(Medicamento medicamento) {
        this.medicamento = medicamento;
    }
    public Consulta getConsulta() {
        return consulta;
    }

    public void setConsulta(Consulta consulta) {
        this.consulta = consulta;
    }

}