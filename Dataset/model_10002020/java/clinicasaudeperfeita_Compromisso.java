





import java.util.List;
import java.util.ArrayList;

public class clinicasaudeperfeita_Compromisso  {

    private String data;
    private String descricao;
    private String hora;



    public clinicasaudeperfeita_Compromisso(
        String data,        String descricao,        String hora    ) {
        this.data = data;
        this.descricao = descricao;
        this.hora = hora;
    }


    public String getData() {
        return data;
    }

    public void setData(String data) {
        this.data = data;
    }
    public String getDescricao() {
        return descricao;
    }

    public void setDescricao(String descricao) {
        this.descricao = descricao;
    }
    public String getHora() {
        return hora;
    }

    public void setHora(String hora) {
        this.hora = hora;
    }


}