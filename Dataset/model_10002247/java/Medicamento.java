





import java.util.List;
import java.util.ArrayList;

public class Medicamento  {

    private String horaInicial;
    private int intervaloTempo;
    private String nome;
    private String descricao;
    private String dataInicio;
    private boolean ativo;
    private String dataFim;





    private Paciente paciente;


    public Medicamento(
        String horaInicial,        int intervaloTempo,        String nome,        String descricao,        String dataInicio,        boolean ativo,        String dataFim    ) {
        this.horaInicial = horaInicial;
        this.intervaloTempo = intervaloTempo;
        this.nome = nome;
        this.descricao = descricao;
        this.dataInicio = dataInicio;
        this.ativo = ativo;
        this.dataFim = dataFim;
    }


    public String getHorainicial() {
        return horaInicial;
    }

    public void setHorainicial(String horaInicial) {
        this.horaInicial = horaInicial;
    }
    public int getIntervalotempo() {
        return intervaloTempo;
    }

    public void setIntervalotempo(int intervaloTempo) {
        this.intervaloTempo = intervaloTempo;
    }
    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }
    public String getDescricao() {
        return descricao;
    }

    public void setDescricao(String descricao) {
        this.descricao = descricao;
    }
    public String getDatainicio() {
        return dataInicio;
    }

    public void setDatainicio(String dataInicio) {
        this.dataInicio = dataInicio;
    }
    public boolean getAtivo() {
        return ativo;
    }

    public void setAtivo(boolean ativo) {
        this.ativo = ativo;
    }
    public String getDatafim() {
        return dataFim;
    }

    public void setDatafim(String dataFim) {
        this.dataFim = dataFim;
    }

    public Paciente getPaciente() {
        return paciente;
    }

    public void setPaciente(Paciente paciente) {
        this.paciente = paciente;
    }

}