





import java.util.List;
import java.util.ArrayList;

public class Atestado  {

    private None consulta;
    private String dataFimDoAtestado;
    private String quantidadeDias;
    private String dataInicioDoAtestado;





    private Consulta consulta;


    public Atestado(
        None consulta,        String dataFimDoAtestado,        String quantidadeDias,        String dataInicioDoAtestado    ) {
        this.consulta = consulta;
        this.dataFimDoAtestado = dataFimDoAtestado;
        this.quantidadeDias = quantidadeDias;
        this.dataInicioDoAtestado = dataInicioDoAtestado;
    }


    public None getConsulta() {
        return consulta;
    }

    public void setConsulta(None consulta) {
        this.consulta = consulta;
    }
    public String getDatafimdoatestado() {
        return dataFimDoAtestado;
    }

    public void setDatafimdoatestado(String dataFimDoAtestado) {
        this.dataFimDoAtestado = dataFimDoAtestado;
    }
    public String getQuantidadedias() {
        return quantidadeDias;
    }

    public void setQuantidadedias(String quantidadeDias) {
        this.quantidadeDias = quantidadeDias;
    }
    public String getDatainiciodoatestado() {
        return dataInicioDoAtestado;
    }

    public void setDatainiciodoatestado(String dataInicioDoAtestado) {
        this.dataInicioDoAtestado = dataInicioDoAtestado;
    }

    public Consulta getConsulta() {
        return consulta;
    }

    public void setConsulta(Consulta consulta) {
        this.consulta = consulta;
    }

}